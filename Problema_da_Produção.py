{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Problema da Produção.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNrUlKzTw5Wmr5AOiEGnM6v",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Juniormoraess/Pyomo---OPL/blob/master/Problema_da_Produ%C3%A7%C3%A3o.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Pu96YzKGH_O-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pyomo.environ as pyEnv\n",
        "\n",
        "lucros = [300, 400, 200, 150]\n",
        "pesos = [[0.3, 0.3, 0.25, 0.15], \n",
        "          [0.25, 0.35, 0.3, 0.1],\n",
        "          [0.45, 0.5, 0.4, 0.22],\n",
        "          [0.15, 0.15, 0.1, 0.05]]\n",
        "\n",
        "capacidade = [1000, 1000, 1000, 1000]\n",
        "capacidade_var = [800, 750, 600, 500]\n",
        "m = len(lucros)\n",
        "\n",
        "modelo = pyEnv.ConcreteModel()\n",
        "\n",
        "modelo.Indices = range(m)\n",
        "modelo.Indices2 = range(m)\n",
        "modelo.Variaveis = pyEnv.Var(modelo.Indices, within = pyEnv.NonNegativeReals)\n",
        "modelo.Objetivo = pyEnv.Objective(expr = sum(lucros[i] * modelo.Variaveis[i] for i in modelo.Indices), sense = pyEnv.maximize)\n",
        "##modelo.Rest1 = pyEnv.Constraint(expr = sum(pesos[i][j] * modelo.Variaveis[j] for i in modelo.Indices for j in modelo.Indices2) <= capacidade[i])\n",
        "modelo.Rest1 = pyEnv.Constraint(expr = (pesos[0][0]*modelo.Variaveis[0] + pesos[0][1]*modelo.Variaveis[1] + pesos[0][2]*modelo.Variaveis[2] + pesos[0][3]*modelo.Variaveis[3]) <= 1000)\n",
        "modelo.Rest2 = pyEnv.Constraint(expr = (pesos[1][0]*modelo.Variaveis[0] + pesos[1][1]*modelo.Variaveis[1] + pesos[1][2]*modelo.Variaveis[2] + pesos[1][3]*modelo.Variaveis[3]) <= 1000)\n",
        "modelo.Rest3 = pyEnv.Constraint(expr = (pesos[2][0]*modelo.Variaveis[0] + pesos[2][1]*modelo.Variaveis[1] + pesos[2][2]*modelo.Variaveis[2] + pesos[2][3]*modelo.Variaveis[3]) <= 1000)\n",
        "modelo.Rest4 = pyEnv.Constraint(expr = (pesos[3][0]*modelo.Variaveis[0] + pesos[3][1]*modelo.Variaveis[1] + pesos[3][2]*modelo.Variaveis[2] + pesos[3][3]*modelo.Variaveis[3]) <= 1000)\n",
        "\n",
        "modelo.Rest5 = pyEnv.Constraint(expr = (modelo.Variaveis[0]) <= 800)\n",
        "modelo.Rest6 = pyEnv.Constraint(expr = (modelo.Variaveis[1]) <= 750)\n",
        "modelo.Rest7 = pyEnv.Constraint(expr = (modelo.Variaveis[2]) <= 600)\n",
        "modelo.Rest8 = pyEnv.Constraint(expr = (modelo.Variaveis[3]) <= 500)\n",
        "\n",
        "solver = pyEnv.SolverFactory('glpk', executable = '/usr/bin/glpsol')\n",
        "result_objetivo = solver.solve(modelo, tee = True)\n",
        "\n",
        "lista = list(modelo.Variaveis.keys())\n",
        "print()\n",
        "print()\n",
        "print('Variaveis: ')\n",
        "print()\n",
        "for i in lista:\n",
        "  print(i, '---', modelo.Variaveis[i]())\n",
        "print()\n",
        "print('Valor da função objetivo =', modelo.Objetivo())"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6htg-gxPidal",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}