#! /usr/bin/env python

"""
    This class implements a document called 'oficio circular'
"""

import time
import datetime
from document import Document


class OficioCircular(Document):
    def __init__(
        self,
        num: str,
        date_creation: datetime,
        summary: str,
        text: str,
        deadline: datetime,
        recipients: list,
    ) -> None:
        super().__init__(num, date_creation, summary)
        self.__text = text
        self.__deadline = deadline
        self.__recipients = recipients

    def __str__(self) -> str:
        result = super().__str__()
        result += "Texto " + self.__text + "\n"
        result += (
            "Data limite para envio: " + self.__deadline.strftime("%d/%m/%Y") + "\n"
        )
        result += "Destinatarios: \n"
        result += ", ".join(self.__recipients) + "\n"
        return result

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str) -> None:
        if (text == "") or (text == None):
            raise Exception("Um texto deve ser fornecido!")
        else:
            self.__text == text

    @property
    def deadline(self) -> datetime:
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: datetime) -> None:
        if deadline == None:
            raise Exception("Uma data limite para envio deve ser fornecida")
        else:
            self.__deadline = deadline

    @property
    def recipients(self) -> list:
        return self.__recipients

    @recipients.setter
    def recipients(self, recipients: list) -> None:
        self.__recipients = recipients

    def is_expired(self) -> bool:
        result = self.__is_expired(self)
        return result

    def __is_expired(self) -> bool:
        today = datetime.date.today()
        result = False
        if self.__deadline < today:
            result = True
        return result

    def __send_copy(self) -> None:
        pass
