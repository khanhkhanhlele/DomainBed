
python -m domainbed.scripts.sweep launch\
       --data_dir=./domainbed/data/\
       --output_dir=./train_output\
       --command_launcher local\
       --algorithms CAG1 \
       --datasets PACS \
       --n_hparams 20\
       --n_trials 3\
       --skip_confirmation\
       --wandb\
       --single_test_envs\