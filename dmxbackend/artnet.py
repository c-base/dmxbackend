import logging
import struct

log = logging.getLogger(__name__)


class ArtNetPollReceived(Exception):
    pass

class ArtNetDecodeError(Exception):
    pass


class ArtNetLengthMismatchError(ArtNetDecodeError):
    pass


class ArtNetPacket(object):
    def __init__(self, universe, length, dmx, sequence=0x00, opcode=0x5000, version=14, physical=0x00):
        self.sequence = sequence
        self.physical = physical
        self.universe = universe
        self.dmx = dmx
        self.opcode = opcode
        self.version = version


def encode_artnet_packet(dmx_data: bytearray, sequence: int=0, universe: int=0, net: int=0, subnet: int=0):
    # break early
    if len(dmx_data) != 512:
        raise ValueError("DMX data must be exactly 512 bytes long")
    
    # Magic bytes for the Art-Net header
    artnet_header = bytearray(18 *[0x00])
    artnet_header[0:8] = b'Art-Net'
    # Opcodes and universes
    artnet_header[8] = 0x00  # OpCode MSB
    artnet_header[9] = 0x50  # OpCode LSB (0x0050 for DMX)
    artnet_header[10:12] = struct.pack('>H', 14)  # Protocol version (0)
    artnet_header[12] = sequence
    artnet_header[13] = 0x00 # Physical port (0)
    artnet_header[14] = (subnet << 4 | universe)
    artnet_header[15] = (net & 0xFF)
    # artnet_header[14:16] = struct.pack('>H', universe)  # Universe (0)
    # length, high byte first (should always be 512)
    artnet_header[16:18] = struct.pack('>H', 512)

    # Art-Net packet
    artnet_packet = bytearray()
    for i in artnet_header:
        artnet_packet.append(i)
    for i in dmx_data:
        artnet_packet.append(i)

    return artnet_packet


def decode_artnet_packet(data: bytearray):
    # A DMX packet contains 512 bytes of DMX data every time.
    header = data[:8]
    # id
    artnet_magic = bytearray(b'Art-Net')
    artnet_magic.append(0x0)
    if header != artnet_magic:
        raise ArtNetDecodeError()

    # OP-Code low byte first
    opcode = (data[8] & 0x00FF) | ((data[9] << 8) & 0xFF00)

    if opcode == 0x2000:
        raise ArtNetPollReceived()

    # proto ver high byte first
    version = ((data[10] << 8) & 0xFF00) | (data[11] & 0x00FF)

    # sequence number (0x00 means disable)
    sequence = data[12]

    # physical port
    physical = data[13]

    # universe, low byte first
    try:
        universe = (data[14] & 0x00FF) | ((data[15] << 8) & 0xFF00)
    except:
        log.info("got udp %s" % repr(data))

    # length, high byte first
    length = ((data[16] << 8) & 0xFF00) | (data[17] & 0x00FF)

    raw_dmx = data[18:]
    if len(raw_dmx) != length:
        raise ArtNetLengthMismatchError()

    packet = ArtNetPacket(
        sequence=sequence,
        physical=physical,
        universe=universe,
        length=length,
        dmx=raw_dmx,
        opcode=opcode,
        version=version
    )
    return packet