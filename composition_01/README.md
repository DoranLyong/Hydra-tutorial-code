# Composition example 1

### Composition File-system Structure 

```bash
├── conf
│   ├── config.yaml   # default list 
│   └── dataset
│       ├── cifar10.yaml
│       └── imagenet.yaml
└── my_app.py
```

where `conf/config.yaml`: 

```yaml
defaults:
  - dataset: cifar10
```

`conf/dataset/cifar10.yaml`:

```yaml
 name: cifar10
 path: /datasets/cifar10
```

`conf/dataset/imagenet.yaml`:

```yaml
 name: imagenet
 path: /datasets/imagenet
```



### Default output test 

```bash
~$ python my_app.py 

# the output should be: 
dataset:
  name: cifar10
  path: /datasets/cifar10
```



### Output test by changing the `dataset` name 

```bash
~$ python my_app.py dataset=imagenet

# the output should be: 
dataset:
  name: imagenet
  path: /datasets/imagenet
```





***

### Reference 

[1] [omry/hydra-article-code, github](https://github.com/omry/hydra-article-code/tree/master/composition) / 여기 코드 참고 <br/>
[2] [Config path changes, hydra.cc](https://github.com/omry/hydra-article-code/tree/master/composition)  / Hydra 1.0 부터 `config.yaml` 경로를 선언하는 방식이 바뀜 <br/>
[3] [The Defaults List, hydra.cc](https://hydra.cc/docs/next/advanced/defaults_list/) /  <br/>
[4] [Extending Configs, hydra.cc](https://hydra.cc/docs/next/patterns/extending_configs) / 

