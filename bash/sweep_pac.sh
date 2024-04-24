
python -m domainbed.scripts.sweep launch\
       --data_dir=./domainbed/data/\
       --output_dir=./train_output\
       --command_launcher dummy\
       --algorithms CAG1 \
       --datasets PACS \
       --n_hparams 1\
       --n_trials 1\
       --skip_confirmation\
       --wandb\
       --single_test_envs\
       --wandb_project domainbed3\
       --wandb_entity namkhanh2172\