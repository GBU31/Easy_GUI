from os import system


if __name__ == '__main__':
    project_name = input('project name:')
    system(f'git clone https://github.com/brookehorizon/EasyGUI && mv EasyGUI {project_name}')
