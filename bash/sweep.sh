# cd ..
# delete_incomplete
# RotatedMNIST ColoredMNIST
# ERM GradBase CAG Fish
# CUDA_VISIBLE_DEVICES=1\ 
python3 -m domainbed.scripts.sweep delete_incomplete\
       --data_dir=./domainbed/data/MNIST/\
       --output_dir=./train_output\
       --command_launcher local\
       --algorithms CAG1 \
       --datasets RotatedMNIST ColoredMNIST\
       --n_hparams 20\
       --n_trials 3\
       --skip_confirmation\
       --wandb\
       --single_test_envs\
