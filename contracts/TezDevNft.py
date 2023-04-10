import smartpy as sp

FA2 = sp.io.import_script_from_url(
    "https://smartpy.io/templates/fa2_lib.py"
)
Utils = sp.io.import_script_from_url(
    "https://raw.githubusercontent.com/RomarQ/tezos-sc-utils/main/smartpy/utils.py"
)

class TezDevNFT(FA2.Admin, FA2.Fa2Nft):
    def __init__(self, metadata, admin, price):
        FA2.Fa2Nft.__init__(self, metadata)
        FA2.Admin.__init__(self, admin)
        self.update_initial_storage(price = price)

    @sp.entry_point
    def publicMint(self):
        sp.verify(sp.amount >= sp.utils.nat_to_mutez(self.data.price),
                      "INSUFFICIENT AMOUNT OF TEZOS")

        token_id = self.data.last_token_id
        metadata = sp.map({
            "":  sp.utils.bytes_of_string("https://gateway.pinata.cloud/ipfs/QmRj2GC9evHerFyg8i8F7deu3D4UTuuUTcwmsiYwjLQsPD")
        })
        self.data.token_metadata[token_id] = sp.record(
            token_id=token_id, token_info=metadata
        )
        self.data.ledger[token_id] = sp.sender
        self.data.last_token_id += 1

    @sp.entry_point
    def ownerMint(self, recipient):
        sp.verify(self.data.administrator == sp.sender, "NOT AN OWNER")

        token_id = self.data.last_token_id
        metadata = sp.map({
            "":  sp.utils.bytes_of_string("https://gateway.pinata.cloud/ipfs/QmRj2GC9evHerFyg8i8F7deu3D4UTuuUTcwmsiYwjLQsPD")
        })
        self.data.token_metadata[token_id] = sp.record(
            token_id=token_id, token_info=metadata
        )
        self.data.ledger[token_id] = recipient
        self.data.last_token_id += 1

    @sp.entry_point
    def setPrice(self, price):
        sp.verify(self.data.administrator == sp.sender, "NOT AN OWNER")
        sp.verify(price > 0, "INVALID PRICE")

        self.data.price = price

@sp.add_test(name = "Test tezDevNft")
def test():
    sc = sp.test_scenario()
    tezDevNft = TezDevNFT(
        metadata = sp.utils.metadata_of_url(
            "https://gateway.pinata.cloud/ipfs/QmRj2GC9evHerFyg8i8F7deu3D4UTuuUTcwmsiYwjLQsPD"
        ),
        admin=sp.address("tz1gX4BdwYdwoyKGwUQjrSLJf3961eh9zgnX"),
        price = 500000
    )
    sc += tezDevNft

sp.add_compilation_target("tezDevNFT", TezDevNFT(
        metadata = sp.utils.metadata_of_url(
            "https://gateway.pinata.cloud/ipfs/QmRj2GC9evHerFyg8i8F7deu3D4UTuuUTcwmsiYwjLQsPD"
        ),
        admin=sp.address("tz1gX4BdwYdwoyKGwUQjrSLJf3961eh9zgnX"),
        price = 500000
    )
)