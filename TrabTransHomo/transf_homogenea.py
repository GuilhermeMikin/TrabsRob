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
            print('Trabalhos Robótica'.center(80))
            print('-'*80)
            sel = input("""
Serviços: 
1- Translação 
2- Translações sucessivas 
3- Rotação 
4- Rotações sucessivas 
5- Translação e rotação sucessivas 
6- Parâmetros de Denavit Hartenberg 2D 
7- Parâmetros de Denavit Hartenberg 3D 
8- Cinemática Inversa
9- Sair 
Serviço N°: """)
            
            if sel == '1':
                print('\nDigite o ponto P(X,Y,Z) a ser transladado!')
                pontoP_X = int(input("X: "))
                pontoP_Y = int(input("Y: "))
                pontoP_Z = int(input("Z: "))
                tx = 2; ty = 3; tz = 5
                ponto_a_ser_transladado = np.array([pontoP_X, pontoP_Y, pontoP_Z, 1])
                vetor_translacao = np.array([tx, ty, tz, 1])
                novo_ponto = translacao(vetor_translacao, ponto_a_ser_transladado)[0]
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
                    novo_ponto = translacao(vetor_translacao1, ponto_a_ser_transladado)[0]
                    novo_ponto2 = translacao(vetor_translacao2, novo_ponto)[0]
                
                    print("Resultado transformação sucessiva de TO.T1 no ponto P:\n")
                    print(f"           |1 0 0 {t0_X0}|   |1 0 0 {t1_X1}|   |{px:2d}|   |{(int(novo_ponto2[0])):3d}|")
                    print(f"P(T0.T1) = |0 1 0 {t0_Y0}| X |0 1 0 {t1_Y1}| X |{py:2d}| = |{(int(novo_ponto2[1])):3d}|")
                    print(f"           |0 0 1 {t0_Z0}|   |0 0 1 {t1_Z1}|   |{pz:2d}|   |{(int(novo_ponto2[2])):3d}|")
                    print(f"           |0 0 0 {1}|   |0 0 0 {1}|   | 1|   |{(int(novo_ponto2[3])):3d}|")

                    novo_ponto3 = translacao(vetor_translacao2, ponto_a_ser_transladado)[0]
                    novo_ponto4 = translacao(vetor_translacao1, novo_ponto3)[0]

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
                novo_ponto_rot = rotacao(anguloteta, eixo, ptP_a_ser_rotacionado)[0]               
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
                novo_ponto_rot = rotacao(anguloteta, eixorot1, ptP_a_ser_rotacionado)[0]
                novo_ponto_rot2 = rotacao(anguloalfa, eixorot2, novo_ponto_rot)[0]

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
                    novo_ponto_trans = translacao(vetor_translacao, ponto_P)[0]
                    novo_ponto_rot = rotacao(anguloteta, eixorot1, novo_ponto_trans)[0]
                    print(f"               |1 0 0 {tx}|       |{pontoP_X:2d}|   |{(int(novo_ponto_rot[0])):3d}|")
                    print(f"P' = T.R(P) =  |0 1 0 {ty}| x R x |{pontoP_Y:2d}| = |{(int(novo_ponto_rot[1])):3d}|")
                    print(f"               |0 0 1 {1}|       |{pontoP_Z:2d}|   |{(int(novo_ponto_rot[2])):3d}|")
                    print(f"               |0 0 0 {1}|       | 1|   |{(int(novo_ponto_rot[3])):3d}|")

                    print("\nTransformação sucessiva R.T:\n")
                    pontoP_X = 4; pontoP_Y = 5; pontoP_Z = 7
                    ponto_P = np.array([pontoP_X, pontoP_Y, pontoP_Z, 1])
                    vetor_translacao = np.array([tx, ty, 1, 1])
                    novo_ponto_rot = rotacao(anguloteta, eixorot1, ponto_P)[0]
                    novo_ponto_trans = translacao(vetor_translacao, novo_ponto_rot)[0]
                    print(f"                   |1 0 0 {tx}|   |{pontoP_X:2d}|   |{(int(novo_ponto_trans[0])):3d}|")
                    print(f"P'' = R.T(P) = R x |0 1 0 {ty}| x |{pontoP_Y:2d}| = |{(int(novo_ponto_trans[1])):3d}|")
                    print(f"                   |0 0 1 {1}|   |{pontoP_Z:2d}|   |{(int(novo_ponto_trans[2])):3d}|")
                    print(f"                   |0 0 0 {1}|   | 1|   |{(int(novo_ponto_trans[3])):3d}|")

                    sleep(5)
                    

                except Exception as e:
                    print('ERRO: ', e.args)
            
            elif sel == '6':
                print('\nDigite os parâmetros de Denavit Hartenberg para um robô de dois elos, onde:\n')
                print('                  | \u03B8j   dj   aj   \u03B1j |')
                print('                  | q1    0   a1    0 |')
                print('                  | q2    0   a2    0 |')
                q1 = int(input("\nq1: "))
                q2 = int(input("q2: "))
                a1 = int(input("a1: "))
                a2 = int(input("a2: "))
                
                resultdenavit = denavit2d(q1, q2, a1, a2)

                try:
                    print("\nNovas coordenadas (x,y) do TCP:\n")
                    print(f'A1:\n{resultdenavit[0]}\n')
                    print(f'A2:\n{resultdenavit[1]}\n')
                    print(f'Coords:\n{resultdenavit[2]}\n')

                    sleep(1)
                except Exception as e:
                    print('ERRO: ', e.args)


            elif sel == '7':
                print('\nDigite os parâmetros de Denavit Hartenberg para um robô manipulador 2 DOF em 3D, onde:\n')
                print('              | Elo | \u03B8     \u03B1    l    d |')
                print('              |  1  | \u03B81   +90   0   L1 |')
                print('              |  2  | \u03B82    0   L2    0 |')
                theta1 = int(input("\n\u03B81: "))
                theta2 = int(input("\u03B82: "))
                l1 = int(input("L1: "))
                l2 = int(input("L2: "))
                
                resultdenavit = denavit3d(theta1, theta2, l1, l2)

                try:
                    print("\nNovas coordenadas (x,y) do TCP:\n")
                    print(f'A1:\n{resultdenavit[0]}\n')
                    print(f'A2:\n{resultdenavit[1]}\n')
                    print(f'Coords:\n{resultdenavit[2]}\n')

                    sleep(1)
                except Exception as e:
                    print('ERRO: ', e.args)


            elif sel == '8':
                try:
                    # Entrada dos valores x, y, fi, elo01 e elo02
                    x = float(input("\nDigite o valor de x: "))
                    y = float(input("Digite o valor de y: "))
                    fi = float(input("Digite o valor de orientação do TCP (fi): "))
                    l1 = float(input("Digite o comprimento do elo 01: "))
                    l2 = float(input("Digite o comprimento do elo 02: "))

                    # Chama a função de calculos dos angulos
                    angulos = cinematica_inversa(x, y, fi, l1, l2)

                    # Imprime os valores os angulos na tela
                    print(f'\n\n\nOs ângulos de orientação do TCP são:\n\n\u03B8: {round(angulos[0], 3)}, \u03B82: {round(angulos[1], 3)} e \u03B83: {round(angulos[2], 3)}\n')

                    sleep(5)
                except Exception as e:
                    print('ERRO: ', e.args)


            elif sel == '9':
                confirm_close = input('\nTecle "SIM" para sair: ')
                if confirm_close in 'Ss':
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

def translacao(vetor_translacao, ponto_a_ser_transladado = np.array([1, 1, 1, 1])):
    matriz_idntd = np.array([ [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0] ])
    matriz_trans = np.zeros((matriz_idntd.shape[0], matriz_idntd.shape[1]+1))
    matriz_trans[:,:-1] = matriz_idntd
    matriz_trans[:,-1:] = vetor_translacao.reshape(matriz_idntd.shape[0], 1)
    pt_transladado = np.dot(matriz_trans, ponto_a_ser_transladado)
    return pt_transladado, matriz_trans


def rotacao(teta, eixo, pontop=np.array([1, 1, 1, 1])):
    if eixo in 'xX':
        matrizRot = np.array([ [1, 0, 0, 0], 
                      [0, round(float(cos(radians(teta))),2), round(float(-sin(radians(teta))),2), 0], 
                      [0, round(float(sin(radians(teta))),2), round(float(cos(radians(teta))),2), 0], 
                      [0, 0, 0, 1] ])
    if eixo in 'yY':
        matrizRot = np.array([ [round(float(cos(radians(teta))),2), 0, round(float(sin(radians(teta))),2), 0], 
                      [0, 1, 0, 0], 
                      [round(float(-sin(radians(teta))),2), 0, round(float(cos(radians(teta))),2), 0], 
                      [0, 0, 0, 1] ])
    if eixo in 'zZ':
        matrizRot = np.array([ [round(float(cos(radians(teta))),2), round(float(-sin(radians(teta))),2), 0, 0], 
                      [round(float(sin(radians(teta))),2), round(float(cos(radians(teta))),2), 0, 0], 
                      [0, 0, 1, 0], 
                      [0, 0, 0, 1] ])
                    
    novoponto = np.dot(matrizRot, pontop)
    
    return novoponto, matrizRot


def denavit2d(q1, q2, a1, a2):
    A1 = np.dot(rotacao(q1, 'Z')[1],translacao(np.array([a1, a1, 0, 1]))[1])
    A2 = np.dot(rotacao(q2, 'Z')[1],translacao(np.array([a2, a2, 0, 1]))[1])

    coordenadas = np.dot(A1,A2)

    return A1, A2, coordenadas


def denavit3d(q1, q2, a1, a2):
    A1 = np.dot(rotacao(q1, 'Z')[1],translacao(np.array([a1, a1, 0, 1]))[1])
    A2 = np.dot(rotacao(q2, 'Z')[1],translacao(np.array([a2, a2, 0, 1]))[1])

    coordenadas = np.dot(A1,A2)

    return A1, A2, coordenadas


def cinematica_inversa(x, y, fi, l1, l2):
    
    # Calculos de teta2
    a=(x**2 + y**2 - l1**2 - l2**2)
    b=(2 * l1 * l2)
    c=a/b
    teta2 = acos(c)

    # Condição para calculo de teta1
    if teta2 > 0:
        teta1 = atan2(y,x) - acos((x**2 + y**2 + l1**2 - l2**2)/(2*l1*sqrt(x**2 + y**2)))
    else:
        teta1 = atan2(y,x) + acos((x**2 + y**2 + l1**2 - l2**2)/(2*l1*sqrt(x**2 + y**2)))

    # Calculo de teta 3
    teta3 = fi - (degrees(teta1)+degrees(teta2))

    return degrees(teta1), degrees(teta2), teta3
