from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
            sel = input("Serviços: \n1- Translação \n2- Translações sucessivas \n3- Rotação \n4- Rotações sucessivas \n5- Translação e rotação sucessivas \n6- Parâmetros de Denavit Hartenberg \n7- Sair \nServiço N°: ")
            
            if sel == '1':
                print('\nDigite o ponto P(X,Y,Z) a ser transladado!')
                pontoP_X = int(input("X: "))
                pontoP_Y = int(input("Y: "))
                pontoP_Z = int(input("Z: "))
                tx = 2; ty = 3; tz = 5
                ponto_a_ser_transladado = np.array([pontoP_X, pontoP_Y, pontoP_Z, 1])
                vetor_translacao = np.array([tx, ty, tz, 1])
                novo_ponto = translacao(vetor_translacao, ponto_a_ser_transladado)
                try:
                    print("Matriz de Transformação:\n")
                    print(f"              |1 0 0 {tx}|   |{pontoP_X:2d}|   |{(int(novo_ponto[0])):3d}|")
                    print(f"P'[{tx}, {ty}, {tz}] = |0 1 0 {ty}| X |{pontoP_Y:2d}| = |{(int(novo_ponto[1])):3d}|")
                    print(f"              |0 0 1 {tz}|   |{pontoP_Z:2d}|   |{(int(novo_ponto[2])):3d}|")
                    print(f"              |0 0 0 1|   | 1|   |{(int(novo_ponto[3])):3d}|")

                    sleep(5)
                except Exception as e:
                    print('ERRO: ', e.args)
            
            
            elif sel == '2':
                print('\nDigite a matriz de transformação T0(x0,y0,z0)!')
                t0_X0 = int(input("x0: "))
                t0_Y0 = int(input("y0: "))
                t0_Z0 = int(input("z0: "))

                print('\nDigite a matriz de transformação T1(x1,y1,z1)!')
                t1_X1 = int(input("x1: "))
                t1_Y1 = int(input("y1: "))
                t1_Z1 = int(input("z1: "))
                px = 3; py = 4; pz = 7
                try:
                    ponto_a_ser_transladado = np.array([px, py, pz, 1])
                    vetor_translacao1 = np.array([t0_X0, t0_Y0, t0_Z0, 1])
                    vetor_translacao2 = np.array([t1_X1, t1_Y1, t1_Z1, 1])
                    novo_ponto = translacao(vetor_translacao1, ponto_a_ser_transladado)
                    novo_ponto2 = translacao(vetor_translacao2, novo_ponto)
                
                    print("Resultado transformação sucessiva de TO.T1 no ponto P:\n")
                    print(f"           |1 0 0 {t0_X0}|   |1 0 0 {t1_X1}|   |{px:2d}|   |{(int(novo_ponto2[0])):3d}|")
                    print(f"P(T0.T1) = |0 1 0 {t0_Y0}| X |0 1 0 {t1_Y1}| X |{py:2d}| = |{(int(novo_ponto2[1])):3d}|")
                    print(f"           |0 0 1 {t0_Z0}|   |0 0 1 {t1_Z1}|   |{pz:2d}|   |{(int(novo_ponto2[2])):3d}|")
                    print(f"           |0 0 0 {1}|   |0 0 0 {1}|   | 1|   |{(int(novo_ponto2[3])):3d}|")

                    novo_ponto3 = translacao(vetor_translacao2, ponto_a_ser_transladado)
                    novo_ponto4 = translacao(vetor_translacao1, novo_ponto3)

                    print("\nResultado transformação sucessiva T1.T0 no ponto P:\n")
                    print(f"           |1 0 0 {t1_X1}|   |1 0 0 {t0_X0}|   |{px:2d}|   |{(int(novo_ponto4[0])):3d}|")
                    print(f"P(T1.T0) = |0 1 0 {t1_Y1}| X |0 1 0 {t0_Y0}| X |{py:2d}| = |{(int(novo_ponto4[1])):3d}|")
                    print(f"           |0 0 1 {t1_Z1}|   |0 0 1 {t0_Z0}|   |{pz:2d}|   |{(int(novo_ponto4[2])):3d}|")
                    print(f"           |0 0 0 {1}|   |0 0 0 {1}|   | 1|   |{(int(novo_ponto2[3])):3d}|")

                    sleep(5)
                except Exception as e:
                    print('ERRO: ', e.args)
            
            
            elif sel == '3':
                print('\nDigite o ângulo teta a ser rotacionado em torno do eixo z!')
                anguloteta = int(input("Ângulo: "))
                px = 4; py = 5; pz = 6
                ptP_a_ser_rotacionado = np.array([px, py, pz, 1])
                eixo = 'z'
                novo_ponto_rot = rotacao(anguloteta, eixo.capitalize()[0], ptP_a_ser_rotacionado)
                
                try:
                    print("\nNovas coordenadas:\n")
                    print(f"                   |{px:2d}|   |{(int(novo_ponto_rot[0])):3d}|")
                    print(f"P' = rot(P) = R{eixo} x |{py:2d}| = |{(int(novo_ponto_rot[1])):3d}|")
                    print(f"                   |{pz:2d}|   |{(int(novo_ponto_rot[2])):3d}|")
                    print(f"                   | 1|   |{(1*1):3d}|")

                    sleep(5)
                except Exception as e:
                    print('ERRO: ', e.args)

                    
            elif sel == '4':
                print('\nDigite o ângulo teta e o eixo da primeira rotação (R1)!')
                anguloteta = int(input("Ângulo: "))
                eixorot1 = input("Eixo: ")
                print('\nDigite o ângulo alfa e o eixo da segunda rotação (R2)!')
                anguloalfa = int(input("Ângulo: "))
                eixorot2 = input("Eixo: ")
                px = 6; py = 6; pz = 8
                ptP_a_ser_rotacionado = np.array([px, py, pz, 1])
                novo_ponto_rot = rotacao(anguloteta, eixorot1.capitalize()[0], ptP_a_ser_rotacionado)
                novo_ponto_rot2 = rotacao(anguloalfa, eixorot2.capitalize()[0], novo_ponto_rot)

                try:
                    print("\nNovas coordenadas:\n")
                    print(f"                                    |{px:2d}|   |{(int(novo_ponto_rot2[0])):3d}|")
                    print(f"P' = R1.R2(P) = R1{eixorot1}({anguloteta}°).R2{eixorot2}({anguloalfa}°) x |{py:2d}| = |{(int(novo_ponto_rot2[1])):3d}|")
                    print(f"                                    |{pz:2d}|   |{(int(novo_ponto_rot2[2])):3d}|")
                    print(f"                                    | 1|   |{(1*1):3d}|")

                    sleep(5)
                except Exception as e:
                    print('ERRO: ', e.args)

            
            elif sel == '5':
                print('\nDigite x e y da matriz de translação T!')
                tx = int(input("X: "))
                ty = int(input("Y: "))
                print('\nDigite o ângulo teta e o eixo da rotação R!')
                anguloteta = int(input("Ângulo: "))
                eixorot1 = input("Eixo: ")

                try:
                    print("\nTransformação sucessiva T.R:\n")
                    pontoP_X = 4; pontoP_Y = 5; pontoP_Z = 7
                    ponto_P = np.array([pontoP_X, pontoP_Y, pontoP_Z, 1])
                    vetor_translacao = np.array([tx, ty, 1, 1])
                    novo_ponto_trans = translacao(vetor_translacao, ponto_P)
                    novo_ponto_rot = rotacao(anguloteta, eixorot1.capitalize()[0], novo_ponto_trans)
                    print(f"               |1 0 0 {tx}|       |{pontoP_X:2d}|   |{(int(novo_ponto_rot[0])):3d}|")
                    print(f"P' = T.R(P) =  |0 1 0 {ty}| x R x |{pontoP_Y:2d}| = |{(int(novo_ponto_rot[1])):3d}|")
                    print(f"               |0 0 1 {1}|       |{pontoP_Z:2d}|   |{(int(novo_ponto_rot[2])):3d}|")
                    print(f"               |0 0 0 {1}|       | 1|   |{(int(novo_ponto_rot[3])):3d}|")

                    print("\nTransformação sucessiva R.T:\n")
                    pontoP_X = 4; pontoP_Y = 5; pontoP_Z = 7
                    ponto_P = np.array([pontoP_X, pontoP_Y, pontoP_Z, 1])
                    vetor_translacao = np.array([tx, ty, 1, 1])
                    novo_ponto_rot = rotacao(anguloteta, eixorot1.capitalize()[0], ponto_P)
                    novo_ponto_trans = translacao(vetor_translacao, novo_ponto_rot)
                    print(f"                   |1 0 0 {tx}|   |{pontoP_X:2d}|   |{(int(novo_ponto_trans[0])):3d}|")
                    print(f"P'' = R.T(P) = R x |0 1 0 {ty}| x |{pontoP_Y:2d}| = |{(int(novo_ponto_trans[1])):3d}|")
                    print(f"                   |0 0 1 {1}|   |{pontoP_Z:2d}|   |{(int(novo_ponto_trans[2])):3d}|")
                    print(f"                   |0 0 0 {1}|   | 1|   |{(int(novo_ponto_trans[3])):3d}|")

                    sleep(5)
                    

                except Exception as e:
                    print('ERRO: ', e.args)
            
            elif sel == '6':
                print('\nDigite os parâmetros de Denavit Hartenberg para um robô de dois elos, onde:\n')
                print('                  |\u03B8j   dj   aj   \u03B1j|')
                print('                  |q1    0   a1    0|')
                print('                  |q2    0   a2    0|')
                q1 = int(input("\nq1: "))
                q2 = int(input("q2: "))
                a1 = int(input("a1: "))
                a2 = int(input("a2: "))
                # px = 4; py = 5; pz = 6
                # ptP_a_ser_rotacionado = np.array([px, py, pz, 1])
                # eixo = 'z'
                # novo_ponto_rot = rotacao(anguloteta, eixo.capitalize()[0], ptP_a_ser_rotacionado)
                
                try:
                    print("\nNovas coordenadas (x,y) do TCP:\n")
                    # print(f"                   |{px:2d}|   |{(int(novo_ponto_rot[0])):3d}|")
                    # print(f"P' = rot(P) = R{eixo} x |{py:2d}| = |{(int(novo_ponto_rot[1])):3d}|")
                    # print(f"                   |{pz:2d}|   |{(int(novo_ponto_rot[2])):3d}|")
                    # print(f"                   | 1|   |{(1*1):3d}|")

                    sleep(1)
                except Exception as e:
                    print('ERRO: ', e.args)


            elif sel == '7':
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

def translacao(vetor_translacao, ponto_a_ser_transladado):
    matriz_idntd = np.array([ [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0] ])
    matriz_trans = np.zeros((matriz_idntd.shape[0], matriz_idntd.shape[1]+1))
    matriz_trans[:,:-1] = matriz_idntd
    matriz_trans[:,-1:] = vetor_translacao.reshape(matriz_idntd.shape[0], 1)
    pt_transladado = np.dot(matriz_trans, ponto_a_ser_transladado)
    return pt_transladado


def rotacao(teta, eixo, pontop):
    if eixo == 'X':
        matrizRot = np.array([ [1, 0, 0, 0], 
                      [0, int(cos(radians(teta))), int(-sin(radians(teta))), 0], 
                      [0, int(sin(radians(teta))), int(cos(radians(teta))), 0], 
                      [0, 0, 0, 1] ])
    if eixo == 'Y':
        matrizRot = np.array([ [int(cos(radians(teta))), 0, int(sin(radians(teta))), 0], 
                      [0, 1, 0, 0], 
                      [int(-sin(radians(teta))), 0, int(cos(radians(teta))), 0], 
                      [0, 0, 0, 1] ])
    if eixo == 'Z':
        matrizRot = np.array([ [int(cos(radians(teta))), int(-sin(radians(teta))), 0, 0], 
                      [int(sin(radians(teta))), int(cos(radians(teta))), 0, 0], 
                      [0, 0, 1, 0], 
                      [0, 0, 0, 1] ])
                    
    novoponto = np.dot(matrizRot, pontop)
    
    return novoponto, matrizRot