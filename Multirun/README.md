# Multirun example

### Composition File-system Structure 

```bash
├── conf
│   ├── config.yaml   # default list 
│   ├── dataset
│   │   ├── cifar10.yaml
│   │   └── imagenet.yaml
│   └── optimizer
│       ├── adam.yaml
│       └── nesterov.yaml
└── my_app.py
```

* the structure is the same with the `composition_02`.



### Multirun output test 

```bash
~$ python my_app.py --multirun dataset=imagenet,cifar10 optimizer=adam,nesterov 

# the output should be: 
[2021-10-14 00:57:39,885][HYDRA] Launching 4 jobs locally
[2021-10-14 00:57:39,885][HYDRA] 	#0 : dataset=imagenet optimizer=adam
dataset:
  name: imagenet
  path: /datasets/imagenet
optimizer:
  type: adam
  lr: 0.1
  beta: 0.01

[2021-10-14 00:57:39,950][HYDRA] 	#1 : dataset=imagenet optimizer=nesterov
dataset:
  name: imagenet
  path: /datasets/imagenet
optimizer:
  type: nesterov
  lr: 0.001

[2021-10-14 00:57:40,023][HYDRA] 	#2 : dataset=cifar10 optimizer=adam
dataset:
  name: cifar10
  path: /datasets/cifar10
optimizer:
  type: adam
  lr: 0.1
  beta: 0.01

[2021-10-14 00:57:40,088][HYDRA] 	#3 : dataset=cifar10 optimizer=nesterov
dataset:
  name: cifar10
  path: /datasets/cifar10
optimizer:
  type: nesterov
  lr: 0.001

```

* 경우의 수 4가지 = {imagenet, cifar10} x {adam, nesterov}





***

### Reference 

[1] [omry/hydra-article-code, github](https://github.com/omry/hydra-article-code/tree/master/composition2 ) / 여기 코드 참고 <br/>
[2] [Config path changes, hydra.cc](https://github.com/omry/hydra-article-code/tree/master/composition)  / Hydra 1.0 부터 `config.yaml` 경로를 선언하는 방식이 바뀜 <br/>
[3] [The Defaults List, hydra.cc](https://hydra.cc/docs/next/advanced/defaults_list/) /  <br/>
[4] [Extending Configs, hydra.cc](https://hydra.cc/docs/next/patterns/extending_configs) / <br/>
[5] [Multi-run, hydra.cc](https://hydra.cc/docs/tutorials/basic/running_your_app/multi-run) / 

