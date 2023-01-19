import torch
import random
import numpy as np
from collections import deque
from game_ai import Game

MAX_MEMORY = 100000
BATCH_SIZE = 1000
LR = 0.001 # learning rate

class Agent:
    def __init__(self):
        self.num_games = 0
        self.epsilon = 0 # randomness
        self.gamma = 0 # discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # if memory exceeded memory popped from left
        # TODO: model, trainer


    def get_state(self, game):
        state = game.board_collapsed
        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        pass

    def get_action(self, state):
        pass

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    best_score = 0
    agent = Agent()
    game = Game()

    while True:
        # get old state
        state_old = agent.get_state(game)

        # get action
        final_action = agent.get_action(state_old)

        # execute move and get new state
        reward, done, score = game.play_step()
        state_new = agent.get_state(game)

        # train short memory of agent
        agent.train_short_memory(state_old, final_action, reward, state_new, done)

        # remember
        agent.remember(state_old, final_action, reward, state_new, done)

        if done:
            # train long memory, plot result
            game.reset()
            agent.num_games += 1
            agent.train_long_memory()

            if score > best_score:
                best_score = score
                # TODO: agent.model.save()
            
            print(f"Game: {agent.num_games}, Score: {score}, Best Score: {best_score}")

            # TODO: Plot data

if __name__ == '__main__':
    train()