#include <stdlib.h>
#include <libgpod/gpod.h>

int main() {
    // Specify the path to the iPod mount point
    const char *ipod_mount_point = "/home/becker/ipodmnt";

    // Specify the path to the MP3 file
    const char *mp3_file_path = "/home/becker/6sSiz9JquC9CZVg1g7QVAQ.mp3";

    // Initialize libgpod
    itdb_init();

    // Create a new iPod database object
    Itdb_iTunesDB *itdb = itdb_parse(ipod_mount_point, NULL);
    if (!itdb) {
        fprintf(stderr, "Error: Unable to parse iTunesDB\n");
        itdb_uninit();
        return EXIT_FAILURE;
    }

    // Create a new track and set its properties
    Itdb_Track *track = itdb_track_new();
    track->title = g_strdup("Rote Flaggen");
    track->artist = g_strdup("berq");
    track->album = g_strdup("Rote Flaggen");
    track->filetype = ITDB_FILETYPE_MP3;
    track->location = g_strdup(mp3_file_path);

    // Add the track to the database
    itdb_playlist_add_track(itdb->tracks, track);

    // Write changes back to the iPod
    if (!itdb_write(itdb)) {
        fprintf(stderr, "Error: Unable to write changes to iTunesDB\n");
    }

    // Free resources
    itdb_free(track);
    itdb_free(itdb);
    itdb_uninit();

    return EXIT_SUCCESS;
}
