
# for env in {0..3}; do
#     python -u -m domainbed.scripts.list_top_hparams \
#         --input_dir ./train_output --algorithm CAG1 \
#         --dataset TerraIncognita --test_env $env \
#         --add_bash \
#         --topk 1 \
#         --bash_dir 'tune_hparams/terra.sh'
# done

# for env in {0..6}; do
#     python -u -m domainbed.scripts.list_top_hparams \
#         --input_dir ./train_output --algorithm CAG1 \
#         --dataset DomainNet --test_env $env \
#         --add_bash \
#         --topk 1 \
#         --bash_dir 'tune_hparams/domain.sh'
# done

for env in {0..3}; do
    python -u -m domainbed.scripts.list_top_hparams \
        --input_dir ./train_output --algorithm CAG1 \
        --dataset TerraIncognita --test_env $env \
        --topk 1 \
        --bash_dir 'tune_hparams/terra.sh'\
        --add_bash 
done

# for env in {0..5}; do
#     python -u -m domainbed.scripts.list_top_hparams \
#         --input_dir ./train_output --algorithm CAG1 \
#         --dataset RotatedMNIST --test_env $env \
#         --topk 1 \
#         --bash_dir 'tune_hparams/mnist.sh'\
#         --add_bash 
# done