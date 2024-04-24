
python -m domainbed.scripts.sweep launch\
       --data_dir=./domainbed/data/\
       --output_dir=.Test/ablationMnist\
       --command_launcher local\
       --algorithms CAG1 \
       --datasets ColoredMNIST \
       --n_hparams 1\
       --n_trials 1\
       --skip_confirmation\
       --wandb\
       --single_test_envs\
       --wandb_project DomainBed3\
       --wandb_entity namkhanh2172\
       --ablation "{'cagrad_c':[0.5,0.1,0.05]}"\