require 'wav-file'
dump = open('dump','w')
wav = open("/home/siva/Desktop/tools/My_tool/try.wav")
format = WavFile::readFormat(wav)
chunk = WavFile::readDataChunk(wav)

wav.close

wavs = chunk.data.unpack('s*')
lsb = wavs.map{|sample| sample[0]}.join
flag = lsb[(lsb.index('1'))..-1]
#puts flag
puts [flag].pack('b*')
dump.write([flag].pack('b*'))
