#not wandb
# CUDA_VISIBLE_DEVICES=1 \
python3 -m domainbed.scripts.train\
       --data_dir=./domainbed/data/\
       --algorithm CAG1\
       --dataset ColoredMNIST\
       --test_env 0\
       --steps 5000\
       --hparams_seed 0\
       --trial_seed 0\
       --hparams '{"cagrad_c" :0.1}'
       # --wandb
