import wandb
import os
wandb.login(key="1eac4d04cc3cc4aed9a1409cd8eb7dc0f6537ef2")

out_dir = "./train_output/a3e651a25960f5dc6c75856b4c92392d12" 
run_name = "CAG1_stop_early_" + os.path.basename(out_dir)
path1 = os.path.join(out_dir, 'results.jsonl')
path2 = os.path.join(out_dir, 'out.txt')
wandb.init(project="DomainBed3",
        entity="namkhanh2172",
        name=run_name,
        force=True)
wandb.save(path1)
wandb.save(path2)
