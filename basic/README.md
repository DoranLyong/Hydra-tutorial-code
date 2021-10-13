# Basic example 

### Regular output test 

```bash
~$ python my_app.py

# the output should be: 
dataset:
  name: imagenet
  path: /datasets/imagenet
```



### Output test when [overriding](https://www.google.com/search?q=override&sxsrf=AOaemvJl9YAxxPrqhWh2u89h2wteHVXxQQ%3A1634131422827&source=hp&ei=3t1mYZfUL_CsmAWa-bPgAQ&iflsig=ALs-wAMAAAAAYWbr7k6yS9k1P2tzcJlky2D5I6vJ9Mf0&oq=override&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCAAQsQMQgwEQQzIKCAAQgAQQhwIQFDIECAAQQzILCAAQgAQQsQMQgwEyBAgAEEMyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCABBCxAzoECCMQJzoECAAQAzoQCAAQgAQQhwIQsQMQgwEQFFCmCljKDWCIFmgAcAB4AIABeIgBzwOSAQMwLjSYAQCgAQE&sclient=gws-wiz) any attribute in the `config.yaml`

```bash
~$ python my_app.py dataset.name=hello_world

# the output should be: 
dataset:
  name: hello_world
  path: /datasets/imagenet
```

* 기존 속성이 오버라이드(overridden) 되어 취소되고, CLI 를 통해 새로 입력된 값으로 대체 됨 



***

### Reference 

[1] [omry/hydra-article-code, github](omry/hydra-article-code, github ) / 여기 코드 참고 <br/>
[2] [Config path changes, hydra.cc](https://hydra.cc/docs/next/upgrades/0.11_to_1.0/config_path_changes/)  / Hydra 1.0 부터 `config.yaml` 경로를 선언하는 방식이 바뀜 <br/>
[3] [A simple command-line application, hydra.cc](https://hydra.cc/docs/next/tutorials/basic/your_first_app/simple_cli) / 

