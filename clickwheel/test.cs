using Clickwheel;

var ipod = IPod.GetConnectedIPod();
var track = new NewTrack
{
    FilePath = "/home/becker/git/spotipod/music/1DIqiqN9afvCS2IirZtJ5u.mp3",
    Album = "Kleine Feuer",
    Artist = "Paula Hartmann",
    AlbumArtist = "Paula Hartmann"
    Title = "Disney",
    IsVideo = false,
    Year = 2024,
    DiscNumber = 1,
    TotalDiscCount = 1,
    TrackNumber = 1,
    AlbumTrackCount = 13,
    Genre = "Pop",
};

var addedTrack = ipod.Tracks.Add(track);


// Write changes to iPod
ipod.SaveChanges();