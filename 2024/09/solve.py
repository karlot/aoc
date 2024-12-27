import sys
# from collections import OrderedDict

def analyze_drive(content):
    drive: list[int] = []
    file_map = {}
    file_address = 0
    for i, block in enumerate(content):
        file_size = int(block)
        if i % 2 == 0:
            for _ in range(file_size):
                drive.append(i // 2)
            file_map[i // 2] = (file_address, file_size)
        else:
            for _ in range(file_size):
                drive.append(None)
        file_address += file_size
    return drive, file_map

def scan_empty(drive: list[int]):
    em: dict[int, int] = {}
    started_empty = False
    current_empty_start = None
    for i, b in enumerate(drive):
        if b == None:
            if not current_empty_start:
                current_empty_start = i
            if not started_empty:
                started_empty = True
                em[current_empty_start] = 1
            else:
                em[current_empty_start] += 1
        else:
            current_empty_start = None
            started_empty = False
    return em

def sort_blocks(drive: list[int]) -> list[int]:
    for i in reversed(range(len(drive))):   # Start from back, and find non-empty blocks
        if drive[i] == None: continue
        for j in range(len(drive)):         # Start from front, and find empty space
            if j == i: return drive         # Reached same disk space, all blocks must be sorted
            if drive[j] != None: continue   # Not empty space, cant swap
            drive[j] = drive[i]             # copy data between location and go to next block
            break
        drive[i] = None                     # We need to clear previous block since we moved the data
    assert True, "We should never reach here!"

def sort_files(drive: list[int], fm: dict[int, tuple[int, int]]) -> list[int]:
    em = scan_empty(drive)
    for fid in reversed(fm.keys()):
        sf, lf = fm[fid]
        for ss, ls in em.items():
            if ss > sf: break       # Empty spaces are behind current file!
            if ls < lf: continue    # Current empty space not big enough for current file!
            # Update drive info
            for i in range(lf):
                drive[ss + i] = fid
                drive[sf + i] = None
            em = scan_empty(drive)
            break
    return drive

def calc_checksum(drive: list[int]):
    return sum(pos * id for pos, id in enumerate(drive) if id != None)


def solve(file):
    with open(file, "r") as f:
        content = f.read()
    content = content.strip()
    
    drive, fm = analyze_drive(content)

    print("Part1:", calc_checksum(sort_blocks(drive.copy())))
    print("Part2:", calc_checksum(sort_files(drive.copy(), fm)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
