#!/usr/bin/env python

# Standard library imports
import unittest
import random
import hashlib

# Custom SHA-1 library
import sha1

class TestSha1(unittest.TestCase):
    """TestSha1 class

    Test case for the custom SHA-1 implementation.
    """
    def test_similar(self):
        """Test Similar SHA-1 Inputs

        Tests sets of messages with 1 bit of difference. Ensures that all
        messages produce unique hashes.

        Raises:
            AssertionError if test fails.
        """
        print '\n>>> running: test_similar'
        first_msg = bytearray(get_random_bytes())
        modified_msg = bytearray()

        # Pick a random byte, modify it by one bit
        byte_to_modify = random.randrange(0, len(first_msg))

        for i, byte in enumerate(first_msg):
            augmentor = 1 if i == byte_to_modify else 0
            modified_msg.append(byte + augmentor)

        first_digest = sha1.sha1(str(first_msg))
        modified_digest = sha1.sha1(str(modified_msg))

        print '... test_similar: checking digest differences'
        self.assertNotEqual(first_digest, modified_digest)

        print '... test_similar: success'

    def test_repeatable(self):
        """Test SHA-1 Repeatability

        Runs the SHA-1 hashing function multiple times to ensure the same
        outcome for any identical message input.
        
        Raises:
            AssertionError if test fails.
        """
        print '\n>>> running: test_repeatable'
        msg = bytearray(get_random_bytes())

        first_digest = sha1.sha1(str(msg))
        second_digest = sha1.sha1(str(msg))

        print '... test_repeatable: checking for identical digests'
        self.assertEqual(first_digest, second_digest)

        print '... test_repeatable: success'

    def test_comparison(self):
        """Test SHA-1 Library Accuracy

        Runs the custom SHA-1 hashing function implementation with other
        SHA-1 functions contained in the Python hashlib library.

        Raises:
            AssertionError if test fails.
        """
        print '\n>>> running: test_comparison'
        msg = bytearray(get_random_bytes())

        custom_sha1_digest = sha1.sha1(str(msg))
        stdlib_sha1_digest = hashlib.sha1(str(msg)).hexdigest()

        print '... test_comparison: checking for identical digests'
        self.assertEqual(custom_sha1_digest, stdlib_sha1_digest)

        print '... test_comparison: success'

def get_random_bytes():
    """Get Random Bits

    Generates a sequence of random bits of a random size between 1 and 1000
    bits in the sequence.

    Returns:
        A stream of random bits.
    """
    size = random.randrange(1, 1000)

    for _ in xrange(size):
        yield random.getrandbits(8)

if __name__ == '__main__':
    unittest.main()
