import smartpy as sp

FA2 = sp.io.import_script_from_url(
    "https://smartpy.io/templates/fa2_lib.py"
)

class TezDevNFT(FA2.Fa2Nft):
    @sp.entry_point
    def mint(self, owner, token_info):
        token_id = self.data.last_token_id
        self.data.ledger[token_id] = owner
        # self.data.token_metadata[token_id] = 

@sp.add_test(name = "Test tezDevNft")
def test():
    sc = sp.test_scenario()
    tezDevNft = TezDevNFT(
        metadata = sp.utils.metadata_of_url(
            " https://gateway.pinata.cloud/ipfs/QmRj2GC9evHerFyg8i8F7deu3D4UTuuUTcwmsiYwjLQsPD"
        )
    )
    sc += tezDevNft
