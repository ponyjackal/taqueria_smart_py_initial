import smartpy as sp

FA2 = sp.io.import_script_from_url(
    "https://smartpy.io/templates/fa2_lib.py"
)

class TezDevNFT(FA2.Fa2Nft):
    pass

@sp.add_test(name = "Test tezDevNft")
def test():
    sc = sp.test_scenario()
    tezDevNft = TezDevNFT(
        metadata = sp.utils.metadata_of_url(
            "https://gateway.pinata.cloud/ipfs/QmRj2GC9evHerFyg8i8F7deu3D4UTuuUTcwmsiYwjLQsPD"
        )
    )
    sc += tezDevNft

sp.add_compilation_target("tezDevNFT", TezDevNFT(
        metadata = sp.utils.metadata_of_url(
            "https://gateway.pinata.cloud/ipfs/QmRj2GC9evHerFyg8i8F7deu3D4UTuuUTcwmsiYwjLQsPD"
        )
    )
)