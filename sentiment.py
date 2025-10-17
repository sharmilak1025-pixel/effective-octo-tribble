{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "name": "sentiment.py",
      "authorship_tag": "ABX9TyMEr46QnQ8wjTT7XclGWRjC",
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
      "execution_count": 3,
      "metadata": {
        "id": "M-0iHp2l-Zaa",
        "outputId": "8a258a31-b97c-4bd0-dc5b-58c50d009532",
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
            "Sentiment: Positive 😊\n"
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
        "    print(\"Sentiment:\", analyze_sentiment(sample))\n"
      ]
    }
  ]
}