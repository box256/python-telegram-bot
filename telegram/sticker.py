#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015 Leandro Toledo de Souza <leandrotoeldodesouza@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

"""This module contains a object that represents a Telegram Sticker"""

from telegram import PhotoSize, TelegramObject


class Sticker(TelegramObject):
    """This object represents a Telegram Sticker.

    Attributes:
        file_id (str):
        width (int):
        height (int):
        thumb (:class:`telegram.PhotoSize`):
        file_size (int):

    Args:
        file_id (str):
        width (int):
        height (int):
        **kwargs: Arbitrary keyword arguments.

    Keyword Args:
        thumb (Optional[:class:`telegram.PhotoSize`]):
        file_size (Optional[int]):
    """

    def __init__(self,
                 file_id,
                 width,
                 height,
                 **kwargs):
        # Required
        self.file_id = file_id
        self.width = int(width)
        self.height = int(height)
        # Optionals
        self.thumb = kwargs.get('thumb')
        self.file_size = int(kwargs.get('file_size', 0))

    @staticmethod
    def de_json(data):
        """
        Args:
            data (str):

        Returns:
            telegram.Sticker:
        """
        if not data:
            return None

        sticker = dict()

        # Required
        sticker['file_id'] = data['file_id']
        sticker['width'] = data['width']
        sticker['height'] = data['height']
        # Optionals
        sticker['thumb'] = PhotoSize.de_json(data['thumb'])
        sticker['file_size'] = data.get('file_size', 0)

        return Sticker(**sticker)

    def to_dict(self):
        """
        Returns:
            dict:
        """
        data = dict()

        # Required
        data['file_id'] = self.file_id
        data['width'] = self.width
        data['height'] = self.height
        # Optionals
        if self.thumb:
            data['thumb'] = self.thumb.to_dict()
        if self.file_size:
            data['file_size'] = self.file_size

        return data
