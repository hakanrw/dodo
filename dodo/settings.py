#     Dodo - A graphical, hackable email client based on notmuch
#     Copyright (C) 2021 - Aleks Kissinger
#
# This file is part of Dodo
#
# Dodo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Dodo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Dodo. If not, see <https://www.gnu.org/licenses/>.

"""
This module holds settings and sets their default values. The values set
here should be overridden by the user in `~/.config/dodo/config.py`. This
can be done as follows:

.. code-block:: python

  import dodo
  dodo.settings.email_address = 'First Last <me@domain.com>''
  dodo.settings.sent_dir = '~/mail/work/Sent'

The settings :func:`~dodo.settings.email_address` and
:func:`~dodo.settings.sent_dir` are required. Dodo may not work correctly
unless you set them properly. The rest of the settings have reasonable
defaults, as detailed below.
"""

from . import themes

# functional
email_address = ''
"""Your email address (REQUIRED)

This is used both to populate the 'From' field of emails and to (mostly)
avoid CC'ing yourself when replying to all. It can be given as 'NAME <ADDRESS@DOMAIN>'
format."""

sent_dir = ''
"""Where to store sent messages (REQUIRED)

This will usually be a subdirectory of the Maildir sync'ed with
:func:`~dodo.settings.sync_mail_command`."""

editor_command = "xterm -e vim '{file}'"
"""Command used to launch external text editor

This is a shell command, which additionally takes the `{file}` placeholder,
which is passed the name of a temp file being edited while composing an email.
"""

file_browser_command = "nautilus '{dir}'"
"""Command used to launch external file browser

This is a shell command, which additionally takes the `{dir}` placeholder. This
command is used when viewing attachments, which first dumps the attachments to a
temp directory given by `{dir}`, then opens that directory in a file browser.
"""

web_browser_command = ''
"""Web browser to use when clicking links in emails

This should be a single command which expects a URL as its first argument. If this
is an empty string, Dodo will attempt to use the default web browser supplied by
the desktop environment, if it exists.
"""

send_mail_command = 'msmtp -t'
"""Command used to send mail via SMTP

This is a shell command that expects a (sendmail-compatible) email message to be
written to STDIN. Note that it should read the destination from the `From:` header
of the message and not a command-line argument.
"""

sync_mail_command = 'offlineimap'
"""Command used to sync IMAP with local Maildir"""

sync_mail_interval = 300
"""Interval to run :func:`~dodo.settings.sync_mail_command` automatically, in seconds

Set this to -1 to disable automatic syncing.
"""

default_to_html = False
"""Open messages in HTML mode by default, rather than plaintext"""

remove_temp_dirs = 'ask'
"""Set whether to remove temporary directories when closing a panel

Thread panels create temporary directories to open attachments. These can be cleaned up
automatically when a panel (or Dodo) is closed. Possible values are: 'always', 'never',
or 'ask'.
"""

# security
html_block_remote_requests = True
"""Block remote requests for HTML messages

HTML messages, especially from dodgy senders, can display remote content or 'call home'
from embedded image tags or iframes. If set to True, Dodo will not allow these requests.
"""

html_confirm_open_links = True
"""Display a confirmation dialog before opening a link in browser

If this is True, Dodo will display a confirmation dialog showing the *actual* URL that
the web browser will request before opening. This is an extra measure against phishing
or emails opening your web browser without your permission.
"""

# visual
theme = themes.nord
"""The GUI theme

A theme is a dictionary mapping a dozen or so named colors to HEX values.
Several themes are defined in `dodo.themes`, based on the popular Nord
and Solarized color palettes.
"""

search_font = 'DejaVu Sans Mono'
"""The font used for search output and various other list-boxes"""

search_font_size = 13
"""The font size used for search output and various other list-boxes"""

message_font = 'DejaVu Sans Mono'
"""The font used for plaintext messages"""

message_font_size = 12
"""The font size used for plaintext messages"""

search_view_padding = 1
"""A bit of spacing around each line in the search panel"""

tag_icons = {
  'inbox': '',
  'unread': '',
  'attachment': '',
  'sent': '>',
  'replied': '',
  'flagged': '',
  'marked': '',
  'signed': '',
}
"""Tag icons

This is a dictionary of substitutions used to abbreviate common tag names as unicode
icons in the search and thread panels.
"""

message_css = """
pre {{
  font-family: {message_font};
  font-size: {message_font_size}pt;
}}

pre .quoted {{
  color: {fg_dim};
}}

pre .headername {{
  color: {fg_bright};
  font-weight: bold;
}}

pre .headertext {{
  color: {fg_bright};
}}

body {{
  background-color: {bg};
  color: {fg};
}}

::-webkit-scrollbar {{
  background: {bg};
}}

::-webkit-scrollbar-thumb {{
  background: {bg_button};
}}

::selection {{
  color: {bg};
  background: {fg};
}}

a {{
  color: {fg_bright};
}}
"""
"""CSS used in view and compose window

Placeholders may be included in curly brackets for any color named in the current theme, as
well as {message_font} and {message_font_size}. Literal curly braces should be doubled, i.e.
'{' should be '{{' and '}' should be '}}'.
"""
