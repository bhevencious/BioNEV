import BioNEV

bionev --input ./data/DrugBank_DDI/DrugBank_DDI.edgelist --output ./embeddings/DeepWalk_DrugBank_DDI.txt --method DeepWalk --task link-prediction --eval-result-file eval_result.txt
bionev --input ./data/DrugBank_DDI/DrugBank_DDI.edgelist --output ./embeddings/DeepWalk_DrugBank_DDI.txt --method struc2vec --task link-prediction --eval-result-file eval_result.txt