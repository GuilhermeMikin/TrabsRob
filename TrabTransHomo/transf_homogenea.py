import math
from time import sleep

class Cliente():
    """
    Classe Cliente MODBUS 
    """
    def atendimento(self):
        """
        Método para atendimento do usuário
        """
        atendimento = True
        while atendimento:
            print()
            print('-'*80)
            print('Transformações Homogêneas'.center(80))
            print('-'*80)
            sel = input("Serviços: \n1- Translação \n2- Translações sucessivas \n3- Rotação \n4- Rotações sucessivas \n5- Translação e rotação sucessivas \n6- Sair \nServiço N°: ")
            if sel == '1':
                print('\nDigite o ponto P(X,Y,Z) a ser transladado!')
                pontoP_X = int(input("X: "))
                pontoP_Y = int(input("Y: "))
                pontoP_Z = int(input("Z: "))
                try:
                    print("Matriz de Transformação:")
                    print(f"              |1 0 0 2|   |{pontoP_X:2d}|   |{(pontoP_X+2):3d}|")
                    print(f"P'[2, 3, 5] = |0 1 0 3| X |{pontoP_Y:2d}| = |{(pontoP_Y+3):3d}|")
                    print(f"              |0 0 1 5|   |{pontoP_Z:2d}|   |{(pontoP_Z+5):3d}|")
                    print(f"              |0 0 0 1|   | 1|   |{(1*1):3d}|")
                    sleep(5)
                except Exception as e:
                    print('ERRO: ', e.args)
            elif sel == '2':
                print('\nDigite a matriz de transformação T0(x0,y0,z0)!')
                pontoP_X0 = int(input("x0: "))
                pontoP_Y0 = int(input("y0: "))
                pontoP_Z0 = int(input("z0: "))
                print('\nDigite a matriz de transformação T1(x1,y1,z1)!')
                pontoP_X1 = int(input("x1: "))
                pontoP_Y1 = int(input("y: "))
                pontoP_Z1 = int(input("z1: "))
                try:
                    print("Resultado transformação sucessiva: ")
                    print(f"        |1 0 0 {pontoP_X0+pontoP_X1}|   |{pontoP_X:2d}|   |{(pontoP_X+2):3d}|")
                    print(f"T0.T1 = |0 1 0 {pontoP_Y0+pontoP_Y1}| X |{pontoP_Y:2d}| = |{(pontoP_Y+3):3d}|")
                    print(f"        |0 0 1 {pontoP_Z0+pontoP_Z1}|   |{pontoP_Z:2d}|   |{(pontoP_Z+5):3d}|")
                    print(f"        |0 0 0 {1}|   | 1|   |{(1*1):3d}|")
                    sleep(5)
                except Exception as e:
                    print('ERRO: ', e.args)
            elif sel == '3':
                print('\nDigite o ângulo teta a ser rotacionado em torno do eixo z!')
                anguloteta = int(input("Ângulo: "))
                try:
                    print("Novas coordenadas: ")
                    xlinha = (math.cos())
                    print()
                except Exception as e:
                    print('ERRO: ', e.args)
            elif sel == '4':
                print('\nDigite o ângulo teta da primeira rotação R1!')
                anguloteta = int(input("Ângulo: "))
                print('\nDigite o ângulo alfa da segunda rotação R2!')
                anguloteta = int(input("Ângulo: "))
                try:
                    print("Novas coordenadas: ")
                except Exception as e:
                    print('ERRO: ', e.args)
            elif sel == '5':
                print('\nDigite o a matriz de translação T(X,Y,Z) a ser transladado!')
                pontoP_X = int(input("X: "))
                pontoP_Y = int(input("Y: "))
                pontoP_Z = int(input("Z: "))
                print('\nDigite o ângulo teta da primeira rotação R!')
                anguloteta = int(input("Ângulo: "))
                try:
                    print("Transformação sucessiva T.R: ")
                    print("Transformação sucessiva R.T: ")
                except Exception as e:
                    print('ERRO: ', e.args)
            elif sel == '6':
                confirm_close = input('\nTecle "SIM" para sair: ').capitalize()[0]
                if confirm_close == 'S':
                    sleep(0.2)
                    print('\nSaindo...\n')
                    sleep(1)
                    atendimento = False
                else:
                    print('\nVoltando..')
                    sleep(2)
            else:
                print('Not found..\n')
                sleep(0.7)