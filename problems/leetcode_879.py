"""
Problem: https://leetcode.com/problems/profitable-schemes/description/?envType=problem-list-v2&envId=50vif4uc
Difficulty: hard
Solved: True
"""

from typing import List


class Solution:

    # Diferente de um problema de algoritmo comum onde buscamos o um valor máximo ou minimo, o problema pede
    # uma contagem de todos os resultados que possíveis a partir de um limite.
    # No problema temos 3 parâmetros para guiar a tomada de decisão do algoritmo, o `index` do crime na lista de crimes, a quantidade membros
    # já alocados em algum crime, e o profit atual.

    # Para cada item na lista devemos então tomar a decisão entre executar o crime ou não.
    # Cada uma das decisões pode gerar n casos em que o `profit` é maior que o mínimo esperado, então devemos contar cada caso e somar o total.
    # Quando o crime não é executado, apenas passamos para o próximo index.
    # Quando o crime é executado, adicionamos o número de pessoas no número de pessoas alocadas, avançamos o index, e adicionamos o profit total.
    # Para diminuir a quantidade de células no array a serem analizadas, podemos limitar o profit em min(profit + profit[i], minProfit)

    def __init__(self) -> None:
        self.dp = []
        self.group = []
        self.crimes = []
        self.group_size = -1
        self.min_profit = -1

        self.mod = 10**9 + 7

    def solve(self, idx: int, group: int, profit: int) -> int:
        # No caso base, se o index chegou no final da lista,
        # Apenas avaliamos se o profit gerado é maior que o mínimo almejado ou não
        # Se for, incrementamos ele como um crime próvavel na solução.
        if idx >= len(self.crimes):
            return 1 if profit >= self.min_profit else 0

        # Se essa combinação de parâmetros já foi calculada, apenas retornamos o valor.
        if self.dp[idx][group][profit] != -1:
            return self.dp[idx][group][profit]

        # Aqui vamos contar quantos esquemas são possíveis se o grupo não escolher esse crime.
        total = self.solve(idx + 1, group, profit)

        # Aqui vamos contar quantos são possíveis se o grupo ainda tiver pessoas disponíveis e decidir cometer o crime.
        if (group + self.group[idx]) <= self.group_size:
            total += self.solve(
                idx + 1,
                group + self.group[idx],
                # Aqui limitamos o profit ao `minProfit` para diminuir a quantidade de células a avaliar.
                min(self.crimes[idx] + profit, self.min_profit),
            )

        # Salvando e retornando o resultado
        self.dp[idx][group][profit] = total % self.mod
        return self.dp[idx][group][profit]

    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        self.min_profit = minProfit
        self.group_size = n
        self.group = group
        self.crimes = profit

        # O array de DP nesse problema tem 3 dimensões de acordo com a quantidade de parâmetros
        # O indíce do crime
        # O número de pessoas alocadas
        # O profit
        for _ in range(len(profit) + 1):
            group_count = []
            for _ in range(n + 1):
                group_count.append([-1] * (minProfit + 1))
            self.dp.append(group_count)

        self.solve(0, 0, 0)
        return self.dp[0][0][0]


if __name__ == "__main__":
    from pprint import pprint

    n = 10
    minProfit = 5
    group = [2, 3, 5]
    profit = [6, 7, 8]

    s = Solution()
    result = s.profitableSchemes(n=n, minProfit=minProfit, group=group, profit=profit)
    pprint(result)
