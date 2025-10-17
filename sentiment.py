{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "name": "sentiment.py",
      "authorship_tag": "ABX9TyNPULgq98tb+ShgBGv2rJFa",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/sharmilak1025-pixel/effective-octo-tribble/blob/main/sentiment.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "M-0iHp2l-Zaa",
        "outputId": "723f8bb0-5f92-4212-c6fe-e695a246ed96",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Input: The product works as expected. Nothing extraordinary.\n",
            "Sentiment: Positive 😊\n",
            "Sharmila\n"
          ]
        }
      ],
      "source": [
        "from textblob import TextBlob\n",
        "\n",
        "def analyze_sentiment(text):\n",
        "    blob = TextBlob(text)\n",
        "    polarity = blob.sentiment.polarity\n",
        "    if polarity > 0:\n",
        "        return \"Positive 😊\"\n",
        "    elif polarity < 0:\n",
        "        return \"Negative 😠\"\n",
        "    else:\n",
        "        return \"Neutral 😐\"\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    sample = \"The product works as expected. Nothing extraordinary.\"\n",
        "    print(\"Input:\", sample)\n",
        "    print(\"Sentiment:\", analyze_sentiment(sample))\n",
        "    print(\"Sharmila1\")\n"
      ]
    }
  ]
}