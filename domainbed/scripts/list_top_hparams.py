# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

"""
Example usage:
python -u -m domainbed.scripts.list_top_hparams \
    --input_dir domainbed/misc/test_sweep_data --algorithm ERM \
    --dataset VLCS --test_env 0
"""

import collections


import argparse
import functools
import glob
import pickle
import itertools
import json
import os
import random
import sys

import numpy as np
import tqdm

from domainbed import datasets
from domainbed import algorithms
from domainbed.lib import misc, reporting
from domainbed import model_selection
from domainbed.lib.query import Q
import warnings

def todo_rename(records, selection_method, latex):

    grouped_records = reporting.get_grouped_records(records).map(lambda group:
        { **group, "sweep_acc": selection_method.sweep_acc(group["records"]) }
    ).filter(lambda g: g["sweep_acc"] is not None)

    # read algorithm names and sort (predefined order)
    alg_names = Q(records).select("args.algorithm").unique()
    alg_names = ([n for n in algorithms.ALGORITHMS if n in alg_names] +
        [n for n in alg_names if n not in algorithms.ALGORITHMS])

    # read dataset names and sort (lexicographic order)
    dataset_names = Q(records).select("args.dataset").unique().sorted()
    dataset_names = [d for d in datasets.DATASETS if d in dataset_names]

    for dataset in dataset_names:
        if latex:
            print()
            print("\\subsubsection{{{}}}".format(dataset))
        test_envs = range(datasets.num_environments(dataset))

        table = [[None for _ in [*test_envs, "Avg"]] for _ in alg_names]
        for i, algorithm in enumerate(alg_names):
            means = []
            for j, test_env in enumerate(test_envs):
                trial_accs = (grouped_records
                    .filter_equals(
                        "dataset, algorithm, test_env",
                        (dataset, algorithm, test_env)
                    ).select("sweep_acc"))
                mean, err, table[i][j] = format_mean(trial_accs, latex)
                means.append(mean)
            if None in means:
                table[i][-1] = "X"
            else:
                table[i][-1] = "{:.1f}".format(sum(means) / len(means))

        col_labels = [
            "Algorithm", 
            *datasets.get_dataset_class(dataset).ENVIRONMENTS,
            "Avg"
        ]
        header_text = (f"Dataset: {dataset}, "
            f"model selection method: {selection_method.name}")
        print_table(table, header_text, alg_names, list(col_labels),
            colwidth=20, latex=latex)

    # Print an "averages" table
    if latex:
        print()
        print("\\subsubsection{Averages}")

    table = [[None for _ in [*dataset_names, "Avg"]] for _ in alg_names]
    for i, algorithm in enumerate(alg_names):
        means = []
        for j, dataset in enumerate(dataset_names):
            trial_averages = (grouped_records
                .filter_equals("algorithm, dataset", (algorithm, dataset))
                .group("trial_seed")
                .map(lambda trial_seed, group:
                    group.select("sweep_acc").mean()
                )
            )
            mean, err, table[i][j] = format_mean(trial_averages, latex)
            means.append(mean)
        if None in means:
            table[i][-1] = "X"
        else:
            table[i][-1] = "{:.1f}".format(sum(means) / len(means))

    col_labels = ["Algorithm", *dataset_names, "Avg"]
    header_text = f"Averages, model selection method: {selection_method.name}"
    print_table(table, header_text, alg_names, col_labels, colwidth=25,
        latex=latex)

def gen_bash_file(arg,hparams):
    command = f"CUDA_VISIBLE_DEVICES=1 \
        python -m domainbed.scripts.train\
        --data_dir {arg['data_dir']}\
        --dataset {arg['dataset']}\
        --algorithm {arg['algorithm']}\
        --test_envs {args.test_env}\
        --output_dir Test/{arg['output_dir']}\
        --trial_seed {arg['trial_seed']}\
        --hparams_seed {arg['hparams_seed']}\
        --seed {arg['seed']}\
        --hparams '{json.dumps(hparams)}'\
        --checkpoint_freq 2000\
        --steps 30001"
    return command
if __name__ == "__main__":
    np.set_printoptions(suppress=True)

    parser = argparse.ArgumentParser(
        description="Domain generalization testbed")
    parser.add_argument("--input_dir", required=True)
    parser.add_argument('--dataset', required=True)
    parser.add_argument('--algorithm', required=True)
    parser.add_argument('--test_env', type=int, required=True)
    parser.add_argument('--topk', type=int, default=0)
    parser.add_argument('--add_bash', action='store_true')
    parser.add_argument('--bash_dir', type=str, default='tune_hparams/bash_hparams.sh')
    args = parser.parse_args()

    records = reporting.load_records(args.input_dir)
    print("Total records:", len(records))

    records = reporting.get_grouped_records(records)
    records = records.filter(
        lambda r:
            r['dataset'] == args.dataset and
            r['algorithm'] == args.algorithm and
            r['test_env'] == args.test_env
    )

    SELECTION_METHODS = [
        model_selection.IIDAccuracySelectionMethod,
        # model_selection.LeaveOneOutSelectionMethod,
        model_selection.OracleSelectionMethod,
    ]
    bash_dir = args.bash_dir

    for selection_method in SELECTION_METHODS:
        print("---------------------------------")
        print(f'Model selection: {selection_method.name}')

        for group in records:
            print(f"trial_seed: {group['trial_seed']}")
            best_hparams = selection_method.hparams_accs(group['records'])
            if args.topk == 0 :
                for run_acc, hparam_records in best_hparams:
                    print(f"\t{run_acc}", end='')
                    # for r in hparam_records:
                        # assert(r['hparams'] == hparam_records[0]['hparams'])
                    # print("\t\thparams:")
                    for k, v in sorted(hparam_records[0]['hparams'].items()):
                        if(k in {"cagrad_c", "cag_update", "meta_lr"}):
                            print('\t{}: {}'.format(k, v), end='')
                    print('\t{}: {}'.format('hparams_seed', hparam_records[0]['args']['hparams_seed']))       
                    # print("")
                    # print("\t\toutput_dirs:")
                    # output_dirs = hparam_records.select('args.output_dir').unique()
                    # for output_dir in output_dirs:
                    #     print(f"\t\t\t{output_dir}")
            else:
                for i in range(args.topk):
                    print(f"Top {i+1}")
                    run_acc, hparam_records = best_hparams[i]
                    print(run_acc)
                    # print(hparam_records[0]['args'])
                    # print(hparam_records[0]['hparams'])
                    bash_file = gen_bash_file(hparam_records[0]['args'],hparam_records[0]['hparams'])
                    print(bash_file)
                    if args.add_bash:
                        with open (bash_dir,'a') as f:
                            f.write("\n")
                            f.write(bash_file)