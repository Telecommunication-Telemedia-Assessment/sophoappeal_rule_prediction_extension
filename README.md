# Extension of photo rule prediction using DNNs
Predicting the usage of photo rules using image tags from Flickr.

This repository is part of [Sohpappeal](https://github.com/Telecommunication-Telemedia-Assessment/sophoappeal).
Please use the main repository as starting point.

This repository is part of the DFG project [Sophoappeal (437543412)](https://www.tu-ilmenau.de/universitaet/fakultaeten/fakultaet-elektrotechnik-und-informationstechnik/profil/institute-und-fachgebiete/fachgebiet-audiovisuelle-technik/forschung/dfg-projekt-sophoappeal).

## Requirements

* python3, python3-pip, git, imagemagick, wget

* recommendation: create a virtual environment: `python3 -m venv venv && source venv/bin/activate`
* install pip3 requirements: `pip3 install -r requirements.txt`
* (`environment.yml` is the exported conda environment used for the training as a backup)

* run `./prepare.sh` to get the pre-trained models.


## Dataset
In `data/rules_2` the urls for the images are stored, use the provided `do_all.sh` script to download the images and pre-process them.
Afterwards run `convert.sh` in `data` to convert the images to smaller resolutions.

On request, we can also share the exact images used for the training.

## Scripts and usage

* `check_results.ipynb`: evaluation of the model predictions used for the paper
* `evaluate_models_multiclass.py` : training code
* `predict.py` : predict rule for images using a pre-trained model

## Usage `evaluate_models_multiclass.py`

```
usage: evaluate_models_multiclass.py [-h] [--data DATA] [--models_folder MODELS_FOLDER] [--results_folder RESULTS_FOLDER] [--epochs EPOCHS] [--no_gpu]
                                     [--batch_size BATCH_SIZE] [--check_images] [--model_idx_start {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}]
                                     [--model_idx_end {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}]

dnn evaluation for multiple image aesthetic rules

optional arguments:
  -h, --help            show this help message and exit
  --data DATA           data to be used (default: data/rules_2_small)
  --models_folder MODELS_FOLDER
                        folder to store best models (default: models/rules_2_small)
  --results_folder RESULTS_FOLDER
                        folder to store results of best models (default: results/rules_2_small)
  --epochs EPOCHS       number of epochs per model (default: 150)
  --no_gpu              do not use gpu (default: False)
  --batch_size BATCH_SIZE
                        size of batches (default: 512)
  --check_images        check input images first (default: False)
  --model_idx_start {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
                        start index of the model which should be used (default: 0)
  --model_idx_end {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
                        end index of the model which should be used (default: 16)

stg7, rasmus 2022
```

## Usage `predict.py`
```
usage: predict.py [-h] [--image_folder IMAGE_FOLDER]
                  [--report_name REPORT_NAME] [--model MODEL]

predict

optional arguments:
  -h, --help            show this help message and exit
  --image_folder IMAGE_FOLDER
                        folder where images are stored (default:
                        data/avt_image_db/jpg/)
  --report_name REPORT_NAME
                        report name of predictions (default:
                        prediction_rules.json)
  --model MODEL         model to be used (default:
                        models/rules_2_small/ResNet50_best_model.hdf5)

stg7 2023
```


## Acknowledgments

If you use this software or data in your research, please include a link to the repository and reference the following papers.

```bibtex
@inproceedings{goering2023ruleext,
  author={Steve {G{\"o}ring} and Rasmus Merten and Alexander Raake},
  title="DNN-based Photo Rule Prediction using Photo Tags",
  booktitle="15th International Conference on Quality of Multimedia Experience (QoMEX)",
  year={2023},
  note={to appear}
}

@article{goering2023imageappeal,
  title={Image Appeal Revisited: Analysis, new Dataset and Prediction Models},
  author={Steve G\"oring and Alexander Raake},
  journal={IEEE Access},
  year={2023},
  publisher={IEEE},
  note={to appear}
}
```

## License
GNU General Public License v3. See [LICENSE.md](./LICENSE.md) file in this repository.

