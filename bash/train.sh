#not wandb
# CUDA_VISIBLE_DEVICES=1 \
# python3 -m domainbed.scripts.train\
#        --data_dir=./domainbed/data/\
#        --algorithm Fishr\
#        --dataset ColoredMNIST\
#        --test_env 0\
#        --steps 5000\
#        --hparams_seed 0\
#        --trial_seed 0\
#        # --wandb

python -m domainbed.scripts.train        --data_dir ./domainbed/data/MNIST/        --dataset ColoredMNIST        --algorithm CAG1        --test_envs 0        --output_dir ./train_output/5999731e60b5277e116e7b1fd386fe0ex        --trial_seed 1        --hparams_seed 45        --seed 303808647        --hparams '{"batch_size": 238, "cag_update": 1, "cagrad_c": 0.5, "class_balanced": false, "data_augmentation": true, "lr": 3.242084701659047e-05, "meta_lr": 0.05, "nonlinear_classifier": false, "resnet18": false, "resnet_dropout": 0.5, "weight_decay": 0.0}'