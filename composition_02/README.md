# Composition example 2

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

where `conf/config.yaml`: 

```yaml
defaults:
  - dataset: cifar10
  - optimizer: adam
```

`conf/optimizer/adam.yaml`:

```yaml
type: adam
lr: 0.1
beta: 0.01
```

`conf/optimizer/nesterov.yaml`:

```yaml
type: nesterov
lr: 0.001
```



### Default output test 

```bash
~$ python my_app.py 

# the output should be: 
dataset:
  name: cifar10
  path: /datasets/cifar10
optimizer:
  type: adam
  lr: 0.1
  beta: 0.01
```



### Output test by changing the `optimizer` name 

```bash
~$ python my_app.py optimizer=nesterov

# the output should be: 
dataset:
  name: cifar10
  path: /datasets/cifar10
optimizer:
  type: nesterov
  lr: 0.001
```

***

### Reference 

[1] [omry/hydra-article-code, github](https://github.com/omry/hydra-article-code/tree/master/composition2 ) / 여기 코드 참고 <br/>
[2] [Config path changes, hydra.cc](https://github.com/omry/hydra-article-code/tree/master/composition)  / Hydra 1.0 부터 `config.yaml` 경로를 선언하는 방식이 바뀜 <br/>
[3] [The Defaults List, hydra.cc](https://hydra.cc/docs/next/advanced/defaults_list/) /  <br/>
[4] [Extending Configs, hydra.cc](https://hydra.cc/docs/next/patterns/extending_configs) / 

