import time

andares = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

while True:
  meuAndar = int(input("\nQUAL ANDAR VOCÊ ESTÁ:  "))
  print("\n" + 20 * "=")
  if meuAndar > 0: # O ELEVADOR ENCONTRA-SE NO TÉRREO, AO SER CHAMADO NO ANDAR SUPERIOR A ZERO
    andares.sort(reverse=False)
    for andar in andares:
      if andar > 0 and andar < meuAndar:
        print(f" ↑ {andar}")
        time.sleep(1.5)
      elif andar == meuAndar:
        print(f"{andar}º ANDAR. EMBARQUE!\n" + 20 * "=")
        andarDestino = meuAndar
    elevador = input("\nVAZIO? - (S/N):  ").upper()
    if elevador == "S":
      elevador = 0
      andares.sort(reverse=True)
      print("\nELEVADOR VOLTANDO PARA O TÉRREO!")
      for a in andares:
        if a < andarDestino and a > 0:
          print(f" ↓ {a}")
          time.sleep(1.5)
        elif a == 0:
          print("TÉRREO!\n" + 20 * "=")
          break
      continue
    else:
      pass

  else: # CASO O ELEVADOR SEJA CHAMADO NO ZERO (TÉRREO)
    print("\nEMBARQUE!\n")
    print(20 * "=")

  while elevador == "N":
    if elevador == "S":
      break
    else:
      andarDestino = int(input("\nQUAL ANDAR DESEJA IR:  "))
      print("\n" + 20 * "=")
      if andarDestino == 0: # AO CHEGAR NO ANDAR ONDE O ELEVADOR FOI CHAMADO, CASO O DESTINO SEJA O ZERO (TÉRREO)
        andares.sort(reverse=True) # [15, 14, 13, 12...]
        for a in andares:
          if a > 0 and a < meuAndar:
            print(f" ↓ {a}")
            time.sleep(1.5)
          elif a == andarDestino:
              print("TÉRREO. DESEMBARQUE!\n" + 20 * "=")
              meuAndar = andarDestino
              elevador = input("\nVÁZIO? - (S/N):  ").upper()
              if elevador == "S":
                break
              else:
                continue
      elif andarDestino != 0 and andarDestino > meuAndar: # AO CHEGAR NO ANDAR QUE O ELEVADOR FOI CHAMADO CASO O ANDAR SEJA SUPERIOR AO ANDAR ATUAL
        andares.sort(reverse=False)
        for a in andares:
          if a > meuAndar and a < andarDestino:
            print(f" ↑ {a}")
            time.sleep(1.5)
          elif a == andarDestino:
              print(f"{a}º ANDAR. DESEMBARQUE!\n" + 20 * "=")
              meuAndar = andarDestino
              elevador = input("\nVÁZIO? - (S/N):  ").upper()
              if elevador == "S":
                elevador = 0
                andares.sort(reverse=True)
                print("\nELEVADOR VOLTANDO PARA O TÉRRO!")
                for a in andares:
                  if a < andarDestino and a > 0:
                    print(f" ↓ {a}")
                    time.sleep(1.5)
                  elif a == 0:
                    print("TÉRREO!\n" + 20 * "=")
                break
              else:
                continue
      elif andarDestino < meuAndar: # AO CHEGAR NO ANDAR QUE O ELEVADOR FOI CHAMADO, CASO O ANDAR SEJA MENOR E DIFERENTE DE ZERO DO ANDAR ATUAL
        andares.sort(reverse=True) # [15, 14, 13...]
        if meuAndar > andarDestino:
          for a in andares:
            if a > andarDestino and a < meuAndar:
              print(f" ↓ {a}")
              time.sleep(1.5)
            elif a == andarDestino:
                print(f"{a}º ANDAR. DESEMBARQUE!\n" + 20 * "=")
                andarDestino = a
                meuAndar = andarDestino
                elevador = input("\nVÁZIO? - (S/N):  ").upper()
                if elevador == "S":
                  andares.sort(reverse=True) # [15, 14, 13...]
                  print("\nELEVADOR VOLTANDO PARA O TÉRRO!")
                  for a in andares:
                    if a < andarDestino and a > 0:
                      print(f" ↓ {a}")
                      time.sleep(1.5)
                    elif a == 0:
                      print("TÉRREO!\n" + 20 * "=")
                  break
                else:
                  continue