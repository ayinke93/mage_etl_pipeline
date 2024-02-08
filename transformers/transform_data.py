
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    def camel_to_snake(name):
        snake_name = [name[0].lower()]
        for char in name[1:]:
        # If the character is uppercase
            if char.isupper():
                
                # Check if the previous character is not an underscore and also lowercase
                if snake_name[-1] != '_' and snake_name[-1].islower():
                    snake_name.append('_')  # Add an underscore before the uppercase letter
                snake_name.append(char.lower())  # Convert the uppercase letter to lowercase
            else:
                snake_name.append(char)  # Directly append lowercase letters
        result =''.join(snake_name)
        result = result.replace('_i_d', '_id')
        return result


    df= data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date

    print(df.columns)

    df.columns = [camel_to_snake(col) for col in df.columns]

    print(df.shape)

    print(df['vendor_id'].unique())
    

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0

    assert output['trip_distance'].isin([0]).sum() == 0

    assert 'vendor_id' in output.columns

