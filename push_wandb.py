import wandb
import os
wandb.login(key="1eac4d04cc3cc4aed9a1409cd8eb7dc0f6537ef2")

out_dir = "train_output/fa65439b8b543b960d743584c5568aa2x" 
run_name = "CAG1_stop_early_" + os.path.basename(out_dir)
path1 = os.path.join(out_dir, 'results.jsonl')
path2 = os.path.join(out_dir, 'out.txt')
wandb.init(project="DomainBed3",
        entity="namkhanh2172",
        name=run_name,
        force=True)
wandb.save(path1)
wandb.save(path2)
