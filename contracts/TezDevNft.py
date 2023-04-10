import smartpy as sp

FA2 = sp.io.import_script_from_url(
    "https://smartpy.io/templates/fa2_lib.py"
)
Utils = sp.io.import_script_from_url(
    "https://raw.githubusercontent.com/RomarQ/tezos-sc-utils/main/smartpy/utils.py"
)

class TezDevNFT(FA2.Fa2Nft):
    @sp.entry_point
    def mint(self, token_info):
        sp.verify(sp.amount >= sp.tez(5),
                      "INSUFFICIENT AMOUNT OF TEZOS")

        token_id = self.data.last_token_id
        self.data.token_metadata[token_id] = sp.record(
            token_id=token_id, token_info=token_info
        )
        self.data.ledger[token_id] = sp.sender
        self.data.last_token_id += 1

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