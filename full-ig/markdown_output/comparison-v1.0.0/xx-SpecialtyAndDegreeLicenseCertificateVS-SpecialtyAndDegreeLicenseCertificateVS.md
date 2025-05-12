

```
java.lang.NullPointerException
	at org.hl7.fhir.r5.comparison.ValueSetComparer.findInList(ValueSetComparer.java:196)
	at org.hl7.fhir.r5.comparison.ValueSetComparer.compareCompose(ValueSetComparer.java:139)
	at org.hl7.fhir.r5.comparison.ValueSetComparer.compare(ValueSetComparer.java:128)
	at org.hl7.fhir.r5.comparison.ComparisonSession.compare(ComparisonSession.java:87)
	at org.hl7.fhir.igtools.publisher.PreviousVersionComparator.finishChecks(PreviousVersionComparator.java:252)
	at org.hl7.fhir.igtools.publisher.Publisher.checkConformanceResources(Publisher.java:4777)
	at org.hl7.fhir.igtools.publisher.Publisher.loadConformance(Publisher.java:4683)
	at org.hl7.fhir.igtools.publisher.Publisher.createIg(Publisher.java:1006)
	at org.hl7.fhir.igtools.publisher.Publisher.execute(Publisher.java:857)
	at org.hl7.fhir.igtools.publisher.Publisher.main(Publisher.java:10033)
	at org.hl7.fhir.igtools.publisher.utils.PublicationProcess.runBuild(PublicationProcess.java:329)
	at org.hl7.fhir.igtools.publisher.utils.PublicationProcess.doPublish(PublicationProcess.java:231)
	at org.hl7.fhir.igtools.publisher.utils.PublicationProcess.publishInner(PublicationProcess.java:175)
	at org.hl7.fhir.igtools.publisher.utils.PublicationProcess.publish(PublicationProcess.java:61)
	at org.hl7.fhir.igtools.publisher.Publisher.main(Publisher.java:9805)

```