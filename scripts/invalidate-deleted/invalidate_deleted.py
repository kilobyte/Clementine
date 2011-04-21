import clementine

from PyQt4.QtCore import QObject
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QAction


class InvalidateDeleted(QObject):
  """
  TODO: actions which are defined here should be implemented here too instead of delegating
  the responsibility to Playlist Manager. Unfortunately, it cannot be done at this moment
  since using PlaylistItemPtrs in Python crashes Clementine.
  """

  def __init__(self):
    QObject.__init__(self)

    self.invalidate = QAction("invalidate_deleted", self)
    self.invalidate.setText("Grey out deleted songs")
    self.connect(self.invalidate, SIGNAL("activated()"), self.grey_out_activated)

    self.delete = QAction("remove_deleted", self)
    self.delete.setText("Remove deleted songs")
    self.connect(self.delete, SIGNAL("activated()"), self.delete_activated)

    clementine.ui.AddAction('playlist_menu', self.invalidate)
    clementine.ui.AddAction('playlist_menu', self.delete)

  def grey_out_activated(self):
    clementine.playlists.InvalidateDeletedSongs()

  def delete_activated(self):
    clementine.playlists.RemoveDeletedSongs()
		

script = InvalidateDeleted()
