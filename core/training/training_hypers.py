from dataclasses import dataclass

@dataclass()
class TurboZeroHypers:
    learning_rate: float = 1e-4
    replay_memory_size: int = 1000
    replay_memory_min_size: int = 1
    replay_memory_sample_games: bool = True
    policy_factor: int = 1
    minibatch_size: int = 128
    minibatches_per_update: int = 16
    train_episodes_per_epoch: int = 5
    test_episodes_per_epoch: int = 5
    test_improvement_threshold: float = 0.0
    temperature_train: float = 0.8
    temperature_test: float = 0.2
    


    