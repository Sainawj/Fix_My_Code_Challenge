# Sort integer arguments (ascending)

# Initialize an empty array to store sorted integers
result = []

# Iterate through each argument
ARGV.each do |arg|
    # Skip if the argument is not an integer
    next unless arg.match?(/^-?\d+$/)

    # Convert the argument to an integer
    i_arg = arg.to_i

    # Insert the integer at the right position in the sorted array
    is_inserted = false
    result.each_with_index do |num, index|
        if num >= i_arg
            result.insert(index, i_arg)
            is_inserted = true
            break
        end
    end
    result << i_arg unless is_inserted
end

# Output the sorted integers
puts result
