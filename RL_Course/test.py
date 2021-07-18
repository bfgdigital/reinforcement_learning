import gym
env = gym.make("CartPole-v0")
observation = env.reset()
env.render()
env.close()
