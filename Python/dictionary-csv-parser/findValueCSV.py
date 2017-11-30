import csv

# Open the check file in a context manager. This ensures the file will be closed
# correctly if an error occurs.
with open('file2.csv', 'rb') as checkfile:
    checkreader = csv.DictReader(checkfile)

    # This does the real work. The middle line is a generator expression which
    # iterates over each line in the check file. The product code and stock
    # level are extracted from each line, the stock level converted into the
    # result, and the two values put together in a tuple. This is then converted
    # into a dictionary. This dictionary has the product codes as its keys and
    # their result code as its values.
    product_result = dict(
        (v['IDNEW'], v['Getty']) for v in checkreader
    )

# print product_result

# Open the input and output files.
with open('file1.csv', 'rb') as infile:
    with open('outfile.csv', 'wb') as outfile:
        reader = csv.DictReader(infile)

        # Use the same field names for the output file.
        writer = csv.DictWriter(outfile, reader.fieldnames)
        writer.writeheader()

        # Iterate over the products in the input.
        for product in reader:
            # Find the stock level from the dictionary we created earlier. Using
            # the get() method allows us to specify a default value if the SKU
            # does not exist in the dictionary.
            result = product_result.get(product['IDOG'])

            # print product['IDOG'] + "," + result

            # Update the product info.
            product['IDOG'] = result

            # Write it to the output file.
            writer.writerow(product)