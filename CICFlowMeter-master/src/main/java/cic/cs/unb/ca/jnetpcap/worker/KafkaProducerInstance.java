package cic.cs.unb.ca.jnetpcap.worker;

import java.util.Properties;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;

public class KafkaProducerInstance {
	private static Properties props;
	private static Producer<String, String> producer = null;
	
	public static Producer<String, String> getKafkaProducer() {
		if(producer == null) {
			props = new Properties();
			props.put("bootstrap.servers", "localhost:9092");
			props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
			props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

			producer = new KafkaProducer<String, String>(props);

		}
		return producer;
	}
	
	private KafkaProducerInstance() {
		
	}
	
}