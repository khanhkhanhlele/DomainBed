#not wandb
CUDA_VISIBLE_DEVICES=0 python3 -m domainbed.scripts.train\
       --data_dir=./domainbed/data/\
       --algorithm CAG1\
       --dataset RotatedMNIST\
       --test_env 0\
       --steps 5000\
       --hparams_seed 0\
       --trial_seed 0\
       --checkpoint_freq 10\
       --hparams '{"batch_size": 8}'
       # --wandb

