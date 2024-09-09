"""
Problem: https://leetcode.com/problems/reducing-dishes/description/?envType=problem-list-v2&envId=50vif4uc
Difficulty: hard
Solved: True
"""

from typing import List


class Solution:
    def __init__(self) -> None:
        self.dp = []
        self.dishes = []
        self.N = -1

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # Primeiro ordenamos a lista de pratos para que possamos sempre pegar os prator com o melhor valor primeiro.
        satisfaction.sort()
        self.N = len(satisfaction)

        # Aqui populamos a tabela DP que contém a relação Pratos X Tempo do Preparo
        # Todos os valores são iniciados como 0 pois é o caso base. Se não há pratos que satisfaçam os clientes, nenhum prato é preparado.
        self.dp = [[0] * (self.N + 1) for _ in range(self.N + 1)]

        # O processo de decisão aqui se baseia em iterar em cada prato *i* e avaliar entre os tempos de preparo disponíveis
        # qual é a melhor ação a ser tomada de acordo com o total acumulado até o momento.
        # Em cada iteração podemos tomar duas decisões:
        #   - 1) Cozinhar o prato i, retornando o resultado (valor[i] * time) + opt(i+1, time+1)
        #   - 2) Se não cozinhar o prato i, passamos ao resultado do próximo prato no tempo atual: opt(i+1, time)

        # Começamos iterando pelos pratos com o maior valor de satisfação
        for i in range(self.N - 1, -1, -1):
            for time in range(self.N):
                cooking = None
                not_cooking = None

                # Se não decirmos cozinhar o prato, buscamos apenas o resultado do próximo item ou retornamos 0 que é o caso base.
                if (i + 1) < self.N:
                    not_cooking = self.dp[i + 1][time]
                else:
                    not_cooking = 0

                # Conzinhando o prato, somamos o coeficiente obtido com o maxímo valor calculado para o resto dos pratos até o momento.
                if (i + 1) < self.N:
                    cooking = (satisfaction[i] * (time + 1)) + (
                        self.dp[i + 1][time + 1]
                    )
                else:
                    cooking = satisfaction[i] * (time + 1)

                # O valor a ser colocado na tabela é o maior entre os dois calculados.
                self.dp[i][time] = max(cooking, not_cooking)

        return self.dp[0][0]


if __name__ == "__main__":
    from pprint import pprint

    s = Solution()
    v = [-1, -8, 0, 5, -9]
    result = s.maxSatisfaction(v)

    print(result)
    pprint(s.dp)
