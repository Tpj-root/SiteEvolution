import libtorrent as lt

def display_torrent_info(torrent_path):
    info = lt.torrent_info(torrent_path)
    print(f"Torrent Name: {info.name()}")
    print(f"Total Size: {info.total_size()} bytes")
    print(f"Number of Pieces: {info.num_pieces()}")
    print(f"Piece Length: {info.piece_length()} bytes\n")

    # Display trackers
    print("Trackers:")
    trackers = list(info.trackers())  # Convert the iterator to a list
    for tracker in trackers:
        print(f"  - {tracker.url}")
    print(f"Total Trackers: {len(trackers)}\n")


    # Display files
    print("Files:")
    files = info.files()
    for idx in range(files.num_files()):
        f = files.file_path(idx)
        size = files.file_size(idx)
        print(f"  - {f} ({size} bytes)")
    print(f"Number of Files: {files.num_files()}\n")

    # Display other metadata
    print("Other Metadata:")
    print(f"  Comment: {info.comment()}")
    print(f"  Creator: {info.creator()}")
    print(f"  Private Torrent: {'Yes' if info.priv() else 'No'}")

# Run the function
display_torrent_info("2025.torrent")

