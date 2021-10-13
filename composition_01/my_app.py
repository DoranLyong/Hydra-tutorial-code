import hydra
from omegaconf import DictConfig, OmegaConf # (ref) https://hydra.cc/docs/next/tutorials/basic/your_first_app/simple_cli


@hydra.main(config_path="./conf", config_name="config") 
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg)) # OmegaConf.to_yaml is used to transform 'DictConfig' to 'str'
    				   # (ref) https://majianglin2003.medium.com/python-omegaconf-a33be1b748ab


if __name__ == "__main__":
    my_app()
