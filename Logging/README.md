# Logging example

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



### Logging output test 

```bash
~$ python my_app.py 

# the output should be: 
[2021-10-14 01:17:56,007][__main__][INFO] - YAML config
[2021-10-14 01:17:56,008][__main__][INFO] - dataset:
  name: cifar10
  path: /datasets/cifar10
optimizer:
  type: adam
  lr: 0.1
  beta: 0.01
```



`outputs/2021-10-14/01-17-55/my_app.log` 확인 

```yaml
[2021-10-14 01:17:56,007][__main__][INFO] - YAML config
[2021-10-14 01:17:56,008][__main__][INFO] - dataset:
  name: cifar10
  path: /datasets/cifar10
optimizer:
  type: adam
  lr: 0.1
  beta: 0.01
```







***

### Reference 

[1] [Logging, hydra.cc](https://hydra.cc/docs/1.0/tutorials/basic/running_your_app/logging) / <br/>


