using Clickwheel;
using static Clickwheel.IPod;
using static Clickwheel.NewTrack;

IPod ipod = IPod.GetConnectedIPod();
NewTrack track = new NewTrack
{
    FilePath = "01 Run Away With Me.m4a",
    Album = "E•MO•TION",
    Artist = "Carly Rae Jepsen",
    AlbumArtist = "Carly Rae Jepsen",
    Title = "Run Away With Me",
    IsVideo = false,
    ArtworkFile = "album.jpg",
    Year = 2015,
    DiscNumber = 1,
    TotalDiscCount = 1,
    TrackNumber = 1,
    AlbumTrackCount = 12,
    Genre = "Pop",
};

ITrack addedTrack = ipod.Tracks.Add(track);
addedTrack.Rating = new IPodRating(5);

IPlaylist playlist = ipod.Playlists.Add("National Anthems");
playlist.AddTrack(addedTrack);

// Write changes to iPod
ipod.SaveChanges();
