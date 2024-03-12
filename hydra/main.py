import hydra
from omegaconf import DictConfig


@hydra.main(config_name="config", version_base=None, config_path="config")
def main(cfg: DictConfig) -> None:
    print(cfg.model.dropout_rate)
    print(cfg.model.num_heads)


if __name__ == "__main__":
    main()
