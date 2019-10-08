

## 1. Introduction

Traffic jam is becoming a world wide problem. Accidents are one of the most important reason in the traffic jam. If we can find the accident as soon as possible, the traffic jam cause by accidents may solved quickly. 

In this project, a collection of 10-weekday traffic data in Beijing collected by the taxis' GPS from Nov. 15, 2011 to Nov. 28, 2011 is used to build a basic traffic model. The data on Nov. 29, 2011 is used to check the model.

Now, the system can be used on analyzing traffic anomaly in Beijing urban area. If you want to use this system in other places, you need to train you own model with adjusting a bit source codes and replacing the data (OpenStreetMap).

## 2. How to Use

First, Put the current traffic data in ./data/final_test/

Then, run the following commands in the terminal
```
pip3 install numpy sklearn bs4 requests lxml matplotlib
python3 main.py
```

The OSM number of roads are listed in ./data/result

## 3. Matters Needing Attention

Due to the slow reaction of the OpenStreetMap API Server, a static map data has put inside the project and using by the system, which may lead a mismatch mistake. However, an API moudle is provided in the source code. Using the given moudle can solve this problem.

Now, the source code will run whole process in the system. To use the system efficiently, you may run only following codes in the main function:
```
get_Sit.run()
```

## 4. License

```
Copyright 2019 Yupeng Liu, Tianyu Li, Zhijun Chen, Yurui Chang

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## 5. Developer

### Group Leader:
* Yupeng Liu ([@PengFCB](https://github.com/PengFCB)), Beijing University of Technology

### Members:
* Tianyu Li ([@](https://github.com/Heyedanlty)[Heyedanlty](https://github.com/Heyedanlty)), Beihang University (BUAA)
* Zhijun Chen ([@CZJ726](https://github.com/CZJ726)), Hunan Unversity
* Yurui Chang, Sichuan University

### Tutor:
* Xingwu Liu, Institute of Computing Technology, Chinese Academy of Sciences


